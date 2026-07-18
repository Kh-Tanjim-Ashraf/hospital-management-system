from django.urls import path
from account.views import (
    PatientRegistration, 
    UserLogin
)


urlpatterns = [
    path('api/register/', view=PatientRegistration.as_view()),
    path('api/login/', view=UserLogin.as_view()),
]
