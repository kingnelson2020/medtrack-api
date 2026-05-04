from patients.models import Patients
from patients.serializers import PatientSerializers
from rest_framework import viewsets #importing viewsets which handles GET, POST, PUT, DELETE requests

# Create your views class here.
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all() #queryset to retrieve all patient records
    serializer_class = PatientSerializers #specifying the serializer class to use for this viewset