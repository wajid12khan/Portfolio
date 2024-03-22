from django.db import models

class Media(models.Model):
    Name = models.CharField(max_length=100)
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='media/')  # 'media/' is the upload directory

    def __str__(self):
        return self.Name
from django.core.validators import EmailValidator

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, validators=[EmailValidator()])  # Ensure unique and valid email
    number = models.CharField(max_length=20)  # Adjust length as needed
    message = models.TextField()

    def __str__(self):
        return self.name
