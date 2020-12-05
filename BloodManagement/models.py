from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator
# Options
BloodTypes = [
    ('A+','A+'),
    ('A-','A-'),
    ('B+','B+'),
    ('B-','B-'),   
    ('O+','O+'),
    ('O-','O-'),
    ('AB+','AB+'),
    ('AB-','AB-'),
]
# Create Models Here
class Doctor(models.Model):
    name = models.CharField(max_length=20)
    address = models.TextField(max_length=50)
    phone = models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
    specialization = models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse("detail-doctor", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name
    

class Department(models.Model):
    name = models.CharField(max_length=10,unique=True)
    dept_type = models.CharField(max_length=10)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name

class Patient(models.Model):
    name = models.CharField(max_length=20)
    gender = models.CharField(
        choices=[
            ('M','Male'),
            ('F','Female'),
            ('O','Others')
        ],
        max_length=2
    )
    address = models.TextField(max_length=50)
    phone = models.BigIntegerField(validators=[MaxValueValidator(9999999999)])
    condition = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor,null=True,on_delete=models.SET_NULL,related_name='patients')
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    blood_type = models.CharField(choices=BloodTypes,max_length=3)
       
    def __str__(self):
        return self.name

class BloodPacket(models.Model):
    patient= models.OneToOneField(Patient,on_delete=models.SET_NULL,null=True,related_name='blood')
    donor = models.CharField(max_length=10)
    date = models.DateField(auto_now_add=True)
    location = models.TextField(max_length=50)
    blood_type = models.CharField(choices=BloodTypes,max_length=3)

    def __str__(self):
        return self.donor
    
class Staff(models.Model):
    name = models.CharField(max_length=20)
    phone = models.IntegerField(validators=[MaxValueValidator(9999999999)])
    address = models.TextField()
    job = models.CharField(choices=[
        ('IT','IT'),
        ('Elec','Electrician'),
        ('Nurse','Nurse')
    ],max_length=5)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL,null=True,related_name='staff')



