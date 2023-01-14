from django.shortcuts import render
import requests

# Create your views here.
def get_products():
    url = 'https://fakestoreapi.com/products'
    r = requests.get(url , auth=True)
    products = r.json() 
    print (products)
    product_list = []
    for i in products:
        product_list.append(i)
    return product_list
get_products()
