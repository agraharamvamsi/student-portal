import email
from django.db import models

# Create your models here.

class StudentProfile(models.Model):
    student_id=models.IntegerField(primary_key=True)
    full_name=models.CharField(max_length=100)
    gender=models.CharField(max_length=100)
    address=models.TextField()
    email=models.EmailField()
    phone=models.CharField(max_length=10)
    blood_group=models.CharField(max_length=100)
    admissiondate=models.DateField()
    course=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    def __str__(self):
        return self.full_name
    
