from django.urls import path
from account.views import PatientRegistration


urlpatterns = [
    path('api/register/', view=PatientRegistration.as_view())
]
