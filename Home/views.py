from itertools import product
from django.shortcuts import render
from .models import Category,Product
# Create your views here.


def store(request):
  categories = Category.objects.all()
  products = Product.objects.all()
  ctxt = {
    'description' :'this store for shopping',
    'keywords' :'shoping store ecom',
    'title' :'my Sotre',
    'categories' : categories , 
    'products' : products , 
  }
  return render(request, 'Home/store.html',ctxt)