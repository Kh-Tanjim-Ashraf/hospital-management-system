from django.urls import path
from account.views import (
    PatientRegistration, 
    UserLogin,
    RequestPasswordReset,
    UserPasswordReset,
    UserDetail,
)
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    # User Account
    path('api/register/', view=PatientRegistration.as_view()),
    path('api/login/', view=UserLogin.as_view()),
    path('api/token/refresh/', view=TokenRefreshView.as_view()),
    path('api/forgot-password/', view=RequestPasswordReset.as_view()),
    path('api/reset-password/<str:uid>/<str:token>/', view=UserPasswordReset.as_view()),

    # Profile Management
    path('api/profile/', view=UserDetail.as_view()),
]
