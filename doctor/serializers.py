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
        fields = ['id', 'name', 'visiting_fee', 'user_id']

    def create(self, validated_data):
        user_data = validated_data.pop('user_id')
        user_profile = user_data.pop('user_profile')

        # Create `User` instance
        user_instance = User.objects.create(**user_data)

        # Create `User_Profile` instance
        User_Profile.objects.create(user_id=user_instance, **user_profile)

        
        doctor_instance = Doctor.objects.create(user_id=user_instance, **validated_data)
        
        return doctor_instance
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user_id', None)

        # Update `Doctor` model data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        
        # Update the data of `User` & `User_Profile` models
        if user_data:
            user_detail_serializer = UserDetailSerializer(instance=instance.user_id, data=user_data, partial=True)
            user_detail_serializer.is_valid(raise_exception=True)
            user_detail_serializer.save()
        
        return instance