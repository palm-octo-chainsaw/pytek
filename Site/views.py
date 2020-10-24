from django.shortcuts import render

# Create your views here.
def product(req):
    return render(req, 'build/products.html')

def details(req):
    return render(req, 'build/product-details.html')