 
from django.shortcuts import render
from .models import Category,Product 
 
 
# Create your views here.


#  ------------- stor -----------------
def store(request): 
  user = request.user.username
  categories = Category.objects.all()
  products = Product.objects.all()
  ctxt = {
    'description' :'this store for shopping',
    'keywords' :'shoping store ecom',
    'title' :'my Sotre',
    'categories' : categories , 
    'products' : products ,
    'user': user
  }
  return render(request, 'Home/store.html',ctxt)

#  ------------- show category details -----------------
def category_show(request , id):
  categ = Category.objects.get(id =id)
  titel  = categ.titel
  meta_desc = categ.description
  ctxt = {
    'description' :meta_desc,
    'title' :titel,
    'category' : categ , 
  }
  return render(request, 'Home/category_show.html',ctxt)
  
#  ------------- show category details -----------------
def products(request , id):
  prod = Product.objects.get(id =id)
  titel  = prod.titel
  meta_desc = prod.description
  ctxt = {
    'description' :meta_desc,
    'title' :titel,
    'product' : prod , 
  }
  return render(request, 'Home/product.html',ctxt)

