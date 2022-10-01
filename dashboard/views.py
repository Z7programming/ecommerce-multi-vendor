
from accounts.models import Profile
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_exempt
from Home.models import Category, Product, Product_images

from .form import Product_form, Product_images_form

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


#  ------------- Dashboard -----------------
def index(request):
    ctxt = {
        # normal
        'title': f'Dashbord-{request.user}',
        # from db
        'products': Product.objects.all(),
        'prod_images_unice': Product_images_unique,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=(request.user)),
    }
    return render(request, 'index.html', ctxt)


#  ------------- Products -----------------
def products(request):
    ctxt = {
        # normal
        'title': f'Dashbord-{request.user}',
        # from db
        'products': Product.objects.all(),
        'prod_images_unice': Product_images_unique,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=(request.user)),
    }
    return render(request, 'products.html', ctxt)


#  ------------- New Product -----------------
def new_product(request):
    if request.method == 'POST':
        form_product = Product_form(request.POST)
        form_product_imgs = Product_images_form(request.POST, request.FILES)
        if form_product.is_valid() and form_product_imgs.is_valid():
            prod = form_product.cleaned_data['titel']
            product = Product.objects.all().filter(titel=prod).first()
            if product:
                print('sory we have this product')
            else:
                images = request.FILES.getlist('image')
                form_product.save()
                pro = Product.objects.all().filter(titel=prod).first()
                for img in images:
                    Product_images.objects.create(image=img, prod=pro)
                return redirect('dashboard:products')
    else:
        form_product = Product_form()
        form_product_imgs = Product_images_form()
    ctxt = {
        # normal
        'title': 'New Product',
        # from db
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        # forms
        'form_product': form_product,
        'form_product_imgs': form_product_imgs,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=(request.user)),
    }
    return render(request, 'new-product.html', ctxt)


#  ------------- delete Product -----------------
@csrf_exempt
def delete_product(request, id):
    Product.objects.get(id=id).delete()
    ctxt = {
        "status": "ok"
    }
    return JsonResponse(ctxt)


#  ------------- delete Image -----------------
def del_img(request, id):
    Product_images.objects.get(id=id).delete()
    ctxt = {
        "status": "ok"}
    return JsonResponse(ctxt)


#  ------------- Edit Product -----------------
def edit_product(request, id):
    prod = Product.objects.get(id=id)
    prod_images = Product_images.objects.all().filter(slug=prod.slug)
    if request.method == 'POST':
        form_product = Product_form(request.POST)
        form_product_imgs = Product_images_form(request.POST, request.FILES)
        if form_product.is_valid():
            prod.titel = form_product.cleaned_data['titel']
            prod.category = form_product.cleaned_data['category']
            prod.description = form_product.cleaned_data['description']
            prod.price = form_product.cleaned_data['price']
            prod.stockag = form_product.cleaned_data['stockag']
            prod.meta_titel = form_product.cleaned_data['meta_titel']
            prod.meta_description = form_product.cleaned_data['meta_description']
            prod.save()
            images = request.FILES.getlist('image')
            for img in images:
                Product_images.objects.create(image=img, prod=prod)
        return redirect('dashboard:products')
    else:
        form_product = Product_form(instance=prod)
        form_product_imgs = Product_images_form()
    ctxt = {
        # normal
        'title': f'edit-{prod.titel}',
        # forms
        'form_product': form_product,
        'form_product_imgs': form_product_imgs,
        # from db
        'categories': Category.objects.all(),
        'products': Product.objects.all(),
        'prod_images': prod_images,
        'product': prod,
        # user
        'user': request.user,
        'profile': Profile.objects.get(user=(request.user)),
    }
    return render(request, 'new-product.html', ctxt)
