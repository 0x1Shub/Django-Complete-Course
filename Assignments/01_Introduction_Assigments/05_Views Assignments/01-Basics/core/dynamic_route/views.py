from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def greet(request, user):
    return HttpResponse(f'Hello, {user}')
