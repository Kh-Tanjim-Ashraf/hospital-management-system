from rest_framework.views import APIView
from rest_framework.response import Response
from appointment.models import Appointment as AppointmentModel
from appointment.serializers import AppointmentSerializer
from rest_framework import status



class Appointment(APIView):

    def get(self, request):
        appointments = AppointmentModel.objects.all()

        serializer = AppointmentSerializer(appointments, many=True)
        
        data = {
            'message': 'Appointment List',
            'data': serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)