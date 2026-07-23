from rest_framework import serializers
from billing.models import Billing
from django.contrib.auth import get_user_model
from account.serializers import UserDetailSerializer
from doctor.serializers import DoctorSerializer
from appointment.serializers import AppointmentSerializer
from appointment.models import Appointment



User = get_user_model()



class BillingSerializer(serializers.ModelSerializer):

    patient_id = UserDetailSerializer()
    doctor_id = DoctorSerializer()
    appointment = AppointmentSerializer()

    class Meta:
        model = Billing
        fields = ['id', 'patient_id', 'doctor_id', 'appointment', 'consultation_fee', 'discount','total_amount']

    def create(self, validated_data):
        patient_id = validated_data.pop('patient_id', None).pop('email', None)
        doctor_id = validated_data.pop('doctor_id', None).pop('user_id', None).pop('email', None)
        appointment_id = validated_data.pop('appointment', None).pop('id', None)

        patient = User.objects.get(email=patient_id)
        doctor = User.objects.get(email=doctor_id).doctor
        appointment = Appointment.objects.get(pk=appointment_id)

        return Billing.objects.create(
            patient_id=patient,
            doctor_id=doctor,
            appointment=appointment,
            **validated_data
        )