from django.shortcuts import render
import requests
from django.core.paginator import Paginator


def display_products(request, *args, **kwargs):
    url = 'https://fakestoreapi.com/products'
    r = requests.get(url)
    products = r.json()
    # Paginator = Paginator(products , 3)
    return render(request, 'dashboardapp/dashboard.html', {'products': products})
