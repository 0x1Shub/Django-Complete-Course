"""
URL configuration for authentication project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from CRUD.views.fn_based_views import (get_message, create_message, update_message, delete_message, search_messages, partial_update_message)
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/<int:message_id>', get_message),
    path('message/create', csrf_exempt(create_message)),
    path('message/update', csrf_exempt(update_message)),
    path('message/delete', csrf_exempt(delete_message)),
    path('message/search/', csrf_exempt(search_messages)),
    path('partial-update/', csrf_exempt(partial_update_message)),

]
