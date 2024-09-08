from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Prediction(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    patient_name = models.CharField(max_length=100)
    date = models.DateField()
    image  = models.ImageField(upload_to='uploads/')
    prediction = models.CharField(max_length=100)


