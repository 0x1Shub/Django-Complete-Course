from django.urls import path
from . import views

handler404 = 'hello.views.custom_404'

urlpatterns = [
    path('hello/', views.index),

    # 2. Mutiple View and URL Mapping
    path('about/', views.about),
    path('contact/', views.contact),

    # 3. Dynamic Url Parameters
    path('hello/<str:name>/', views.dynamicURL, name='DynamicUrl'),

    # 4. Use template in views 
    path('hello-template/', views.templateUse, name="hello-template"),

    # 5. Pass Dynamic Data to template
    path('hello-template/<str:first_name>/', views.dynamicTemplate),

    # 6. Redirect Views
    path('home/', views.home),

    # 7. Handling 404 Error

]
