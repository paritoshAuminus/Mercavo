from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views
from .views import MeView

urlpatterns = [
    # POST---------------------------------------------
    path('register/', views.register),
    path('login/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    # GET/PATCH----------------------------------------
    path('users/me/', MeView.as_view())
]
