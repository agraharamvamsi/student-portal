from dataclasses import fields
from django import forms
from app.models import *

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model=StudentProfile
        fields='__all__'
        