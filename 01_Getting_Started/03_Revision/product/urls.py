from django.urls import path
from . import views

urlpatterns = [
    path('greet/', views.hello_shubham, name="Hello Shubham")
]