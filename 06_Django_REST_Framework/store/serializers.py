from decimal import Decimal
from rest_framework import serializers
from . import models

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length = 255)
    price = serializers.DecimalField(max_digits = 6, decimal_places = 2)
    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax')

    def calculate_tax(self, product: models.Product):
        return product.unit_price * Decimal(1.1)


# Model Serializers
class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'slug', 'inventory', 'description', 'unit_price', 'collection']
        # fields = '__all__' # Bad Practice

    price_with_tax = serializers.SerializerMethodField(method_name = 'calculate_tax') 

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Collection
        fields = ['id', 'title']

