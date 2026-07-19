from rest_framework import serializers
from doctor.models import Doctor
from account.serializers import UserDetailSerializer
from django.contrib.auth import get_user_model
from account.models import User_Profile



User = get_user_model()



class DoctorSerializer(serializers.ModelSerializer):

    user_id = UserDetailSerializer()

    class Meta:
        model = Doctor
        fields = ['name', 'visiting_fee', 'user_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user_id')
        user_profile = user_data.pop('user_profile')

        # Create `User` instance
        user_instance = User.objects.create(**user_data)

        # Create `User_Profile` instance
        User_Profile.objects.create(user_id=user_instance, **user_profile)

        
        doctor_instance = Doctor.objects.create(user_id=user_instance, **validated_data)
        
        return doctor_instance