from rest_framework import serializers
from billing.models import Billing



class BillingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Billing
        fields = ['id', 'patient_id', 'doctor_id', 'appointment', 'consultation_fee', 'discount','total_amount']