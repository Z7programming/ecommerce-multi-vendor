from unicodedata import category
from django.contrib import admin
from .models import Category ,Product
# Register your models here.
 
admin.site.register([Category , Product])