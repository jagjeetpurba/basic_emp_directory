from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='images')
    designation=models.CharField(max_length=100)
    email=models.EmailField(max_length=50, unique=True)
    phone_number=models.CharField(max_length=12)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name