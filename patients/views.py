from patients.models import Patients
from patients.serializers import PatientSerializers
from rest_framework import viewsets #importing viewsets which handles GET, POST, PUT, DELETE requests


# Create your views class here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all() #queryset to retrieve all patient records
    filterset_fields = ['gender', 'blood_group', 'genotype']
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['created_at', 'date_of_birth', 'weight_kg', 'temperature_celsius', 'blood_pressure_systolic']
    serializer_class = PatientSerializers #specifying the serializer class to use for this viewset