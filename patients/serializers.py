from rest_framework import serializers
from patients.models import Patients


class PatientSerializers(serializers.ModelSerializer):
    # This serializer is used to convert the Patients model instances into JSON format and vice versa.
    # It includes all the fields from the Patients model, as well as two additional fields: age and risk_score, which are calculated using the methods defined in the Patients model.
    age = serializers.SerializerMethodField() # SerializerMethodField is a special type of field that allows you to define a method to calculate the value of the field based on their date of birth.
    risk_score = serializers.SerializerMethodField()
    
    def get_age(self, obj):
        return obj.calculate_age()
        
    def get_risk_score(self, obj):
        return obj.calculate_risk_score()
    
    def validate_blood_pressure_systolic(self, value):
        if value < 60 or value > 250:
            raise serializers.ValidationError(
                'Systolic blood pressure must be between 60 and 250 mmHg.'
            )
        return value
    
    def validate_blood_pressure_diastolic(self, value):
        if value < 40 or value > 150:
            raise serializers.ValidationError(
                'Diastolic blood pressure must be between 40 and 150 mmHg.'
            )
        return value

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
        
        