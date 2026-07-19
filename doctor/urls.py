from django.urls import path
from doctor.views import Doctor


urlpatterns = [
    path('api/doctors/', view=Doctor.as_view())
]
