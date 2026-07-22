from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail
from account.models import User_Profile



User = get_user_model()



class PatientRegistrationSerializer(serializers.ModelSerializer):

    # Since `password2` is not a field of `User` model, we are required to explicitly define this field here
    password2 = serializers.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'password2']
    
    def validate(self, attrs):
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError("The two passwords didn't match")

        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        return User.objects.create_user(**validated_data)



class UserLoginSerializer(serializers.ModelSerializer):

    # Since the `email` field of `User` model raises unique email error if an already existing email is passed from the client, thus an `email` field is explicitly defined here
    email = serializers.EmailField(max_length=255)

    class Meta:
        model = User
        fields = ['email', 'password']



class RequestPasswordResetSerializer(serializers.Serializer):

    email = serializers.EmailField(max_length=255)

    def validate(self, attrs):
        if not User.objects.filter(email=attrs.get('email')).exists():
            raise serializers.ValidationError("No account is associated with this email address")

        user = User.objects.get(email=attrs.get('email'))

        # Build the magic password reset link
        uid = urlsafe_base64_encode(force_bytes(user.id))
        token = default_token_generator.make_token(user)
        link = f"{settings.FRONTEND_URL}/reset-password/{uid}/{token}/"
        
        send_mail(
            subject="Welcome!",
            message=f"Your password reset link is given below:\n{link}",
            from_email=None,
            recipient_list=[user.email],
            fail_silently=False,
        )

        return attrs



# Separate serializer to dedicatedly verify token validation
class UserPasswordResetTokenValidationSerializer(serializers.Serializer):
    
    uid = serializers.CharField(max_length=10)
    token = serializers.CharField(max_length=50)

    def validate(self, attrs):
        # Validate user
        uid = urlsafe_base64_decode(attrs.get('uid'))
        if not User.objects.filter(id=uid).exists():
            raise serializers.ValidationError("Invalid user ID")
            
        user = User.objects.get(id=uid)
        
        # Validate token
        if not default_token_generator.check_token(user, attrs.get('token')):
            raise serializers.ValidationError("Token is invalid or expired")
        
        # Stored the user-record since the child-serializer-class will utilize this record to update a new password against this record
        self.context['user'] = user

        return attrs



# Re-validate token again when the user inputs password & confirm password from frontend form
class UserPasswordResetConfirmSerializer(UserPasswordResetTokenValidationSerializer):

    password1 = serializers.CharField(max_length=255)
    password2 = serializers.CharField(max_length=255)

    def validate(self, attrs):
        # `uid` & `token` is injected into the request.data dictionary from the `POST` api-endpoint

        # Still validate the token from the parent serializer class
        attrs = super().validate(attrs)

        if attrs.get('password1') != attrs.get('password2'):
            raise serializers.ValidationError("The two passwords didn't match")
        
        # Access the user-record from the parent serializer class
        user = self.context.get('user')
        user.set_password(attrs.get('password1'))
        user.save()

        return attrs



class UserProfileSerializer(serializers.ModelSerializer):

    # This field gets optional to be passed as part of the JSON data when hitting the update API when required=False; The `write_only=True` never returns `user_id` in the API response.
    user_id = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User_Profile
        fields = ['id', 'user_id', 'full_name', 'phone', 'address']



class UserDetailSerializer(serializers.ModelSerializer):

    user_profile = UserProfileSerializer()
    email = serializers.EmailField(max_length=255, required=False)

    class Meta:
        model = User
        fields = ['id', 'email', 'role', 'user_profile']
        # Bypass the automatically generated UniqueValidator of DRF for `email` field & let "DoctorSerializer" to execute the `update()` method of it's own class.
        extra_kwargs = {
            "email": {
                "validators": []
            }
        }
    
    def update(self, instance, validated_data):
        # 1. Pop the nested data out of the validated data dictionary
        profile_data = validated_data.pop('user_profile', None)

        # 2. Update the parent fields (User instance)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # 3. Update the nested fields (Profile instance)
        if profile_data is not None:
            profile_instance = instance.user_profile  # Get the related object
            for attr, value in profile_data.items():
                setattr(profile_instance, attr, value)
            profile_instance.save()

        return instance

"""

Note:
=====
There are two main methods for updating date through nested serializer:

Method#1 Using `setattr()` method inside the for-loop of popped out dictionary provided from client.
    # Applied in the `update()` method of `UserDetailSerializer`

Method#2 Passing the popped out dictionary directly into nested serializer as `data` argument, also defined the `partial=True` so that it can handle any n-level of missing data.
    # Applied in the `update()` method of `DoctorSerializer`

***Method#2 is more preferable since it allows code re-usability by adding the updated data through the nested serializer and it will automatically updates any other nested data inside the parent-nested data. 
    i.e. Doctor has 1:1 relationship with User & User has 1:1 relationship with User_Profile. So when passing the new value to update doctor data, if a client wants to update the user/user_profile data, passing the popped out dictionary into the nested serializer of UserDetailSerializer will automatically update the User model data as well as User_Profile model data.

"""