from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Prediction
from django.http import HttpResponse

# Loading Tensorflow to load our model
from tensorflow.keras.models import load_model
from PIL import Image
from django.conf import settings
import os
import numpy as np

def preprocess_image(image):
    img = Image.open(image)
    img = img.resize((299, 299))  # Resize based on model's input shape
    img = np.array(img) / 255.0   # Normalize the image (if your model requires normalization)
    
    if img.ndim == 2:  # Grayscale image
        img = np.stack([img] * 3, axis=-1)  # Convert to RGB by repeating grayscale channel
    elif img.shape[-1] == 4:  # RGBA image
        img = img[..., :3]  # Drop the alpha channel if present
    
    img = np.expand_dims(img, axis=0)  # Add batch dimension
    return img

def login_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, "Invalid username or password")
            return redirect('login_page')
        
        login(request, user)
        return redirect('user_records_with_id', user_id=user.id)

    return render(request, "app/login.html")

@login_required(login_url='login_page')
def user_records(request, user_id):
    if request.user.id != user_id:
        return HttpResponse("You are not authorized to view this page.", status=403)

    MODEL_PATH = os.path.join(settings.BASE_DIR, 'app', 'ml-models', 'pneumonia-model.h5')
    model = load_model(MODEL_PATH)

    user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        patient_name = request.POST.get("patient_name")
        date = request.POST.get("date")
        image = request.FILES.get('image')

        if patient_name and date and image:
            preprocessed_image = preprocess_image(image)
            prediction_result = model.predict(preprocessed_image)
            prediction_prob = prediction_result[0][0]
            print(prediction_prob)
            predicted_class = (prediction_prob > 0.5).astype(int)  # Apply threshold

            prediction_label = "Normal" if predicted_class == 0 else "Pneumonia"


            Prediction.objects.create(
                user=request.user,
                patient_name=patient_name,
                date=date,
                image=image,
                prediction=prediction_label
            )

            return redirect('user_records_with_id', user_id=request.user.id)
        
    records = Prediction.objects.filter(user=user)
    return render(request, "app/user_records.html", {"records": records, "user": user})




def signup_page(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!!")
            return redirect("signup_page")

        # Create the user with hashed password
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully!!")

        # Log the user in immediately after signup
        login(request, user)
        return redirect('user_records_with_id', user_id=user.id)  # Correct redirect

    return render(request, "app/signup.html")


@login_required(login_url="/app/login/")
def delete_record(request, record_id):
    record = get_object_or_404(Prediction, id=record_id)

    if record.user != request.user:
        return HttpResponse("You are not authorized to delete this record.")

    if request.method == "POST":
        record.delete()
        return redirect('user_records_with_id', user_id=request.user.id)
    
    return HttpResponse("Invalid request method.")


def logout_page(request):

    logout(request)
    return redirect("/login/")