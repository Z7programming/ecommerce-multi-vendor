from django.contrib import admin
from .models import Category, Product, Product_images
# Register your models here.

admin.site.register([Category, Product, Product_images])
