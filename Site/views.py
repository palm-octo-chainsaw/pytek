from django.shortcuts import render
from django.views.generic import DetailView
from .models import Product

# Create your views here.

def home(req):
    return render(req, 'build/products.html')

class ProductDetailView(DetailView):
    model = Product
    product = Product.objects.all()
    template_name = 'build/product-details.html', {product:'product'}
