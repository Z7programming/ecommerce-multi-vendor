
from django.utils.text import slugify
from django.db import models

# Create your models here.


class Category (models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    titel = models.CharField(max_length=100, null=True, blank=True, default="")
    description = models.TextField(null=True, blank=True, default="")
    logo = models.ImageField(
        upload_to='categories/logo/', null=True, blank=True)
    show_in_store = models.BooleanField(default=True)
    meta_titel = models.CharField(max_length=100, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        meta_titel_txt = ""
        meta_description_txt = ""
        if len(self.meta_titel) > 0:
            meta_titel_txt = self.meta_titel
        else:
            meta_titel_txt = self.titel
        if len(self.meta_description) > 0:
            meta_description_txt = self.meta_description
        else:
            meta_description_txt = self.description
        self.meta_titel = meta_titel_txt
        self.meta_description = meta_description_txt
        prodtxt = str(self.titel)
        self.slug = slugify(prodtxt)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.titel


class Product (models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    show_in_store = models.BooleanField(default=True)
    titel = models.CharField(max_length=100, default="")
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, default="")
    price = models.DecimalField(default=00.00, max_digits=6, decimal_places=2)
    stockag = models.IntegerField(blank=True, default=1)
    meta_titel = models.CharField(max_length=100, blank=True, default="")
    meta_description = models.TextField(blank=True, default="")
    raiting = models.IntegerField(default=0, blank=True)
    slug = models.SlugField(blank=True)

    def save(self, *args, **kwargs):
        meta_titel_txt = ""
        meta_description_txt = ""
        if len(self.meta_titel) > 0:
            meta_titel_txt = self.meta_titel
        else:
            meta_titel_txt = self.titel
        if len(self.meta_description) > 0:
            meta_description_txt = self.meta_description
        else:
            meta_description_txt = self.description
        self.meta_titel = meta_titel_txt
        self.meta_description = meta_description_txt
        prodtxt = str(self.titel)
        self.slug = slugify(prodtxt)
        super(Product, self).save(*args, **kwargs)

    def __str__(self):
        return self.titel


class Product_images(models.Model):
    prod = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=f'products/images/%y/%m/%d/')
    slug = models.SlugField(null=True, blank=True)

    def save(self, *args, **kwargs):
        prodtxt = str(self.prod)
        self.slug = slugify(prodtxt)
        super(Product_images, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.slug)
