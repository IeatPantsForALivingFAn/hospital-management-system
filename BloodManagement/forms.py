from django import forms
from django.forms import ModelForm
from .models import BloodTypes, Doctor, Department, Patient
# form classes here

class CreateDoctorForm(forms.Form):
    name = forms.CharField(max_length=10)
    address = forms.CharField(widget=forms.Textarea,max_length=50)
    phone = forms.IntegerField()
    specialization = forms.CharField(max_length=20)

class CreateDepartmentForm(forms.Form):
    name = forms.CharField(max_length=10)
    department_type = forms.CharField(max_length=10)
    capacity = forms.IntegerField()

class CreatePatientForm(forms.Form):
    name = forms.CharField(max_length=20)
    gender = forms.ChoiceField(
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Others')
        ]
    )
    address = forms.CharField(widget=forms.Textarea,max_length=50)
    phone = forms.IntegerField()
    condition = forms.CharField(max_length=20)
    blood_type = forms.ChoiceField(choices=BloodTypes)
    department = forms.ModelChoiceField(queryset=Department.objects.all())
    doctor = forms.ModelChoiceField(queryset=Doctor.objects.all())

class CreateBloodForm(forms.Form):
    patient = forms.ModelChoiceField(queryset=Patient.objects.all())
    donor = forms.CharField(max_length=10)
    location = forms.CharField(widget=forms.Textarea,max_length=50)
    blood_type = forms.ChoiceField(choices=BloodTypes)