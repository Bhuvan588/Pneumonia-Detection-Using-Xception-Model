
# Pneumonia-Detection-Using-Xception Model

This project aims to detect whether a person has pneumonia or not by taking an xray image as input. It uses Xception Model for prediction and Django framework for storing and diaplaying records entered by a patient or user.



![WhatsApp Image 2024-09-09 at 12 42 45 AM](https://github.com/user-attachments/assets/a5dcdc36-09ac-4f23-9771-34073cd4bda0)






## Why Xception you may ask?

I was reading about some architectures that have been progressively made over time. Hence I learnt about Xception model. It is an architecture which uses less no of computations that its previous models like Inception because it uses Depthwise Convolutions to reduce the complexity and cost of traditional Convolutions.
![WhatsApp Image 2024-09-09 at 12 45 51 AM](https://github.com/user-attachments/assets/af9c8358-a545-4b12-b78c-44b6fdce53f0)


## Installation

1. Clone the project into your required folder

2. Create a virtual environment using 

python -m venv "your environment name"

3. In your terminal type 

cd project (i.e. the folder inside which the django apps reside)

python manage.py runserver

4. Signup and upload any image to get the prediction 


    
## Features

- Model:  Uses the Xception model trained on chest X-ray images.

- Frontend:  Built with Django templates using Bulma CSS for styling

- Backend:   Django framework to handle user records and image predictions.



## Contributing

Contributions are welcome! If you have suggestions or improvements, please open an issue or submit a pull request

