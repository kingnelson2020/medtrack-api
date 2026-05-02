from django.db import models

# Create your models here.
class Patients(models.Model):
    #data and actions related to patients
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]
    
    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-')
    ]
    
    GENOTYPE_CHOICES = [
        ('AA', 'AA'),
        ('AS', 'AS'),
        ('SS', 'SS'),
        ('AC', 'AC')
    ]
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    blood_group = models.CharField(max_length=3, choices=BLOOD_GROUP_CHOICES)
    genotype = models.CharField(max_length=2, choices=GENOTYPE_CHOICES)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2)
    temperature_celsius = models.DecimalField(max_digits=4, decimal_places=1)
    blood_pressure_systolic = models.IntegerField()
    blood_pressure_diastolic = models.IntegerField()
    current_complaints = models.TextField(blank=True)
    medical_history = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    #string representation of the patient object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
