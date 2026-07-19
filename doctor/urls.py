from django.urls import path
from doctor.views import Doctor, DoctorDetail


urlpatterns = [
    path('api/doctors/', view=Doctor.as_view()),
    path('api/doctor/<int:id>/', view=DoctorDetail.as_view()),
]
