# forms.py

from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['carnet', 'nombres', 'apellidos', 'correo_electronico', 'fecha_nacimiento']
