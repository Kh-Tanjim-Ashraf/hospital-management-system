from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from doctor.models import Doctor
from appointment.models import Appointment



User = get_user_model()



class DashboardSummary(APIView):

    def get(self, request):
        total_patients = User.objects.filter(role='p').count()
        total_doctors = Doctor.objects.count()
        total_appointments = Appointment.objects.count()
        pending_appointments = Appointment.objects.filter(status='pend').count()
        completed_appointments = Appointment.objects.filter(status='comp').count()

        data = {
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "total_appointments": total_appointments,
            "pending_appointments": pending_appointments,
            "completed_appointments": completed_appointments
        }

        return Response(data=data, status=status.HTTP_200_OK)
