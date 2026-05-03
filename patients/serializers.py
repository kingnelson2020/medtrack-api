from rest_framework import serializers
from patients.models import Patients


class PatientSerializers(serializers.ModelSerializer):
    # This serializer is used to convert the Patients model instances into JSON format and vice versa.
    age = serializers.SerializerMethodField()
    risk_score = serializers.SerializerMethodField()
    
    def get_age(self, obj):
        return obj.calculate_age()
        
    def get_risk_score(self, obj):
        return obj.calculate_risk_score()
    
    class Meta:
        # The Meta class is used to specify the model and fields that should be included in the serialization process.
        model = Patients
        fields = [
            "id",
            "first_name",
            "last_name",
            "date_of_birth",
            "gender",
            "blood_group",
            "genotype",
            "weight_kg",
            "temperature_celsius",
            "blood_pressure_systolic",
            "blood_pressure_diastolic",
            "current_complaints",
            "medical_history",
            "created_at",
            "age",
            "risk_score",
        ]
        read_only_fields = ['created_at', 'age', 'risk_score']
        
        