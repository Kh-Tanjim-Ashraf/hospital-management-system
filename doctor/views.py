from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from doctor.models import Doctor as DoctorModel
from django.contrib.auth import get_user_model
from doctor.serializers import DoctorSerializer



User = get_user_model()



class Doctor(APIView):

    def get(self, request):
        doctors = DoctorModel.objects.all()

        serializer = DoctorSerializer(instance=doctors, many=True)

        data = {
            'message': 'Doctor Information',
            'data': serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)