from django.urls import path , include
from .views import display_products

urlpatterns = [
    path('products/', display_products , name='products'),
]
