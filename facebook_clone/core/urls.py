from django.contrib import admin
from django.urls import path
from core.views import auth

urlpatterns = [
    path('', auth, name='login'),
    # Add more URLs as needed
]
