from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.core.mail import send_mail



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



class RequestPassowrdResetSerializer(serializers.Serializer):

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