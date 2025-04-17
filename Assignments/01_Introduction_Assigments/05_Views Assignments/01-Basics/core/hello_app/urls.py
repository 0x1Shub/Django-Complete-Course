from django.urls import path
from . import views

urlpatterns = [
    path('/', views.hello_shubham, name="hello-app")
]