from rest_framework import serializers
from doctor.models import Doctor
from account.serializers import UserDetailSerializer



class DoctorSerializer(serializers.ModelSerializer):

    user_id = UserDetailSerializer()

    class Meta:
        model = Doctor
        fields = ['name', 'visiting_fee', 'user_id']