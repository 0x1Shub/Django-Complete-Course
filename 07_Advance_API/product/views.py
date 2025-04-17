from django.shortcuts import render
from rest_framework.views import APIViews
from rest_framework.http import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Product

# Create your views here.
# Class Based Views
class ProductList(APIViews):
    def get(self, request):
        queryset = Product.objects.select_related('collection').all
        serializer = ProductSerializer(
            queryset, many=True, context={'request': request}
        )
        return Response(serializer.data)

    def post(self, response):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)