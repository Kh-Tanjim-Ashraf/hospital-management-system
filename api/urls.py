from django.urls import path, include
from account.views import (
    PatientRegistration, 
    UserLogin,
    RequestPasswordReset,
    UserPasswordReset,
    UserDetail,
)
from rest_framework_simplejwt.views import TokenRefreshView
from doctor.views import Doctor, DoctorDetail
from appointment.views import Appointment, AppointmentDetail
from billing.views import Billing, BillingDetail
from dashboard.views import DashboardSummary



urlpatterns = [
    # Account
    path('register/', view=PatientRegistration.as_view()),
    path('login/', view=UserLogin.as_view()),
    path('token/refresh/', view=TokenRefreshView.as_view()),
    path('forgot-password/', view=RequestPasswordReset.as_view()),
    path('reset-password/<str:uid>/<str:token>/', view=UserPasswordReset.as_view()),

    # Profile Management
    path('profile/', view=UserDetail.as_view()),

    # Doctor
    path('doctors/', view=Doctor.as_view()),
    path('doctor/<int:id>/', view=DoctorDetail.as_view()),

    # Appointment
    path('appointments/', view=Appointment.as_view()),
    path('appointments/<int:id>/', view=AppointmentDetail.as_view()),

    # Billing
    path('bills/', view=Billing.as_view()),
    path('bills/<int:id>/', view=BillingDetail.as_view()),

    # Dashboard Summary
    path('dashboard/', view=DashboardSummary.as_view())
]