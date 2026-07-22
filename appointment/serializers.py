from rest_framework import serializers
from appointment.models import Appointment
from django.contrib.auth import get_user_model
from account.serializers import UserDetailSerializer
from doctor.serializers import DoctorSerializer



User = get_user_model()



class AppointmentSerializer(serializers.ModelSerializer):

    # The `required=False` argument is to make this serializer suitable for partial update
    patient_id = UserDetailSerializer(required=False)
    doctor_id = DoctorSerializer(required=False)

    class Meta:
        model = Appointment
        fields = ['patient_id', 'doctor_id', 'appointment_date', 'appointment_time', 'status']