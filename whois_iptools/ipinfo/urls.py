from django.urls import path
from . import views

urlpatterns = [
    path('', views.ip_result, name="ipinfo"),
]