from rest_framework import serializers
from appointment.models import Appointment
from django.contrib.auth import get_user_model
from account.serializers import UserDetailSerializer
from doctor.serializers import DoctorSerializer
from doctor.models import Doctor



User = get_user_model()



class AppointmentSerializer(serializers.ModelSerializer):

    # The `required=False` argument is to make this serializer suitable for partial update; Also make these fields as read-only
    patient_id = UserDetailSerializer(required=False)
    doctor_id = DoctorSerializer(required=False)

    class Meta:
        model = Appointment
        fields = ['patient_id', 'doctor_id', 'appointment_date', 'appointment_time', 'status']

    def create(self, validated_data):

        patient_id = validated_data.pop('patient_id', None).pop('email', None)
        doctor_id = validated_data.pop('doctor_id', None).pop('user_id', None).pop('email', None)

        patient = User.objects.get(email=patient_id)
        doctor = User.objects.get(email=doctor_id).doctor

        return Appointment.objects.create(
            patient_id=patient,
            doctor_id=doctor,
            **validated_data
        )