from django.urls import path
from .views.message_views import MessageView

urlpatterns = [
    path('messages/', MessageView.as_view(), name='messages')
]
