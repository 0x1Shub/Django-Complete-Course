from django.urls import path
from . import views

urlpatterns = [
    path('', views.hello_drf, name="Hello DRF"),
]