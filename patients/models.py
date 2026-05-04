from django.db import models
from datetime import date

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
        ('SC', 'SC'),
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
    current_complaints = models.TextField()
    medical_history = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True) #timestamp when the patient record was created
    #string representation of the patient object
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    #method to calculate the age of the patient
    def calculate_age(self):
        today = date.today()
        dob = self.date_of_birth
        age = today.year - dob.year
        if(today.month, today.day) < (dob.month, dob.day):
            age -= 1
        return age
    
    #method to calculate risk score
    def calculate_risk_score(self):
        risk_score = 0
        
        #age checks
        age = self.calculate_age()
        if age > 60:
            risk_score += 2

        # blood pressure checks
        if self.blood_pressure_systolic > 140:
            risk_score += 2
            
        if self.blood_pressure_diastolic > 90:
            risk_score += 2
            
        # temperature checks
        if self.temperature_celsius > 39.5:
            risk_score += 2
        elif self.temperature_celsius > 38.0:
            risk_score += 1

        # genotype check
        if self.genotype in ['SS', 'SC']:
            risk_score += 2
            
        # weight check
        if self.weight_kg > 100:
            risk_score += 2
            
        #return risk level based on score
        if risk_score >= 6:
            return 'High Risk'
        elif risk_score >= 3:
            return 'Medium Risk'
        else:
            return 'Low Risk'
