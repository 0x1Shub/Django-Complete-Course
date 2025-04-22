from django.urls import path
from .views import secure_data

urlpatterns = [
    path('', secure_data)
]