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
    appointment = AppointmentSerializer(required=False)

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

    def update(self, instance, validated_data):
        # Re-organize for partial updates
        patient_id = validated_data.pop('patient_id', None)
        doctor_id = validated_data.pop('doctor_id', None)

        if patient_id:
            patient_email = patient_id.pop('email', None)
            patient = User.objects.get(email=patient_email)
            instance.patient_id = patient

        if doctor_id:
            doctor_email = doctor_id.pop('user_id', None).pop('email', None)
            doctor = User.objects.get(email=doctor_email).doctor
            instance.doctor_id = doctor

        # Note: Each bill has a 1:1 relationship with an appointment, thus changing an appointment id will raise an `IntegrityError`. Cannot change appointment of a bill record.

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        
        return instance