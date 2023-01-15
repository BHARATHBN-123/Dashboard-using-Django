from django.shortcuts import render
import requests


def display_products(request,*args,**kwargs):
    url = 'https://fakestoreapi.com/products'
    r = requests.get(url)
    products = r.json() 

    return render (request , 'dashboardapp/base.html',{'products': products})
