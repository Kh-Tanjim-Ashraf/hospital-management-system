from django.urls import path
from account.views import (
    PatientRegistration, 
    UserLogin
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('api/register/', view=PatientRegistration.as_view()),
    path('api/login/', view=UserLogin.as_view()),
    path('api/token/refresh/', view=TokenRefreshView.as_view()),
]
