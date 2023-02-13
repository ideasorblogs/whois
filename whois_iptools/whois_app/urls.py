from django.urls import path
from . import views

urlpatterns = [
    path('', views.whois_info, name="whois_app"),
]