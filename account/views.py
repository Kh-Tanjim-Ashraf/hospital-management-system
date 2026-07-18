from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from account.serializers import (
    PatientRegistrationSerializer,
    UserLoginSerializer
)
from rest_framework_simplejwt.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate



def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }



class PatientRegistration(APIView):

    def post(self, request):
        serializer = PatientRegistrationSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            patient = serializer.save()
            # Required to generate JWT token for a newly registered user since s/he will be automatically redirected to the dashboard/any page where authenticated access is required
            data = {
                'message': 'Patient created successfully',
                'token': get_tokens_for_user(patient)
            }
            
            return Response(data=data, status=status.HTTP_201_CREATED)



class UserLogin(APIView):

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            user = authenticate(email=email, password=password)

            if user:
                data = {
                    'message': 'Login successful',
                    'token': get_tokens_for_user(user)
                }
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data = {'message': 'Email or password is invalid'}
                return Response(data=data, status=status.HTTP_404_NOT_FOUND)