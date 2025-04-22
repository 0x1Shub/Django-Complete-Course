from django.urls import path
from .views import get_products, product_detail, get_users, user_details

urlpatterns = [
    path('products/', get_products, name='get-products'),
    path('products/<int:pk>/', product_detail, name='product-detail'),
    path('users/', get_users, name='get-users'),
    path('users/<int:pk>', user_details, name='user-detail')
]
