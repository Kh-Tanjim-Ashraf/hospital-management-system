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

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'message': 'Appointment created successfully',
                'data': serializer.data
            }

            return Response(data=data)



class AppointmentDetail(APIView):

    def get(self, request, id):
        appointment = AppointmentModel.objects.get(pk=id)
        serializer = AppointmentSerializer(instance=appointment)
        
        data = {
            'message': 'Appointment information',
            'data': serializer.data
        }

        return Response(data=data, status=status.HTTP_200_OK)

    def put(self, request, id):
        appointment = AppointmentModel.objects.get(pk=id)
        serializer = AppointmentSerializer(instance=appointment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'message': 'Appointment information updated successfully',
                'data': serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)

    
    def patch(self, request, id):
        appointment = AppointmentModel.objects.get(pk=id)
        serializer = AppointmentSerializer(instance=appointment, data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()

            data = {
                'message': 'Appointment information updated successfully',
                'data': serializer.data
            }

            return Response(data=data, status=status.HTTP_200_OK)

    
    # Soft Delete an appoint detail
    def delete(self, request, id):
        appointment = AppointmentModel.objects.get(pk=id)
        appointment.status = 'canc'
        appointment.save()

        return Response(status=status.HTTP_204_NO_CONTENT)