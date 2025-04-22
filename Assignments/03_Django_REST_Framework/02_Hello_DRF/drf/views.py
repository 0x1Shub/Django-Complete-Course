# from django.shortcuts import render
# from django.http import HttpResponse

# # Create your views here.
# def hello_drf(request):
#     return HttpResponse("Hello Shubham")


from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET', 'POST'])

def hello_drf(request, name):
    return Response({"message": f"Hello {name}"})