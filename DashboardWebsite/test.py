import requests


url = 'https://fakestoreapi.com/products'
r = requests.get(url )
products = r.json()

product_list = []
for i in products:
    product_list.append(i)
print(len(product_list))


    
