from django.shortcuts import render

# Create your views here.


def store(request):
  ctxt = {
    'description' :'this store for shopping',
    'keywords' :'shoping store ecom',
    'title' :'my Sotre',
  }
  return render(request, 'Home/store.html',ctxt)