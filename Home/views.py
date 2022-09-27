
from django.shortcuts import render
from .models import Category, Product, Product_images
from accounts.models import Profile


# Create your views here.

#  ----- get first product img -----------------
list_img = list(Product_images.objects.all())
Product_images_unique = []
for x in list_img:
    Product_images_unique.append(x)
for round in range(3):
    for y1 in Product_images_unique:
        for y2 in Product_images_unique:
            ind1 = Product_images_unique.index(y1)
            ind2 = Product_images_unique.index(y2)
            if (ind1 != ind2) and (y1.slug == y2.slug):
                Product_images_unique.pop(ind2)
#  ------------- home -----------------


def home(request):
    ctxt = {
        # normal
        'title': 'home',
        'description': 'this store for shopping',
        'keywords': 'shoping store ecom',
        # from db
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'prod_images':  Product_images.objects.all(),
        'prod_images_unice': Product_images_unique,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=request.user),
    }
    return render(request, 'home.html', ctxt)
#  ------------- shop -----------------


def shop(request):
    ctxt = {
        # normal
        'title': 'Shop',
        'description': 'this store for shopping',
        'keywords': 'shoping store ecom',
        # from db
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'prod_images':  Product_images.objects.all(),
        'prod_images_unice': Product_images_unique,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=request.user),
    }
    return render(request, 'shop.html', ctxt)
#  ------------- product detail -----------------


def product(request, slug):
    product = Product.objects.get(slug=slug)
    ctxt = {
        # normal
        'title': product.titel,
        'description': product.meta_description,
        'keywords': product.meta_titel,
        # from db
        'product': product,
        'product_imgs': Product_images.objects.all().filter(slug=slug),
        'similar_products': Product.objects.all().filter(category=product.category),
        'prod_images_unice': Product_images_unique,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=request.user),
    }
    return render(request, 'product.html', ctxt)
