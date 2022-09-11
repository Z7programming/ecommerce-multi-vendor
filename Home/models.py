from pyexpat import model
from unicodedata import category
from django.db import models

# Create your models here.



class Category (models.Model):
  date_created = models.DateTimeField(auto_now_add=True)
  titel = models.CharField(max_length=100,null=True,blank=True ,default="")
  description = models.TextField(null=True,blank=True ,default="")
  logo = models.ImageField(upload_to= 'categories/logo/',null=True,blank=True)
  show_in_store = models.BooleanField(default=True )
  meta_titel = models.CharField(max_length=100,null=True,blank=True ,default="" )
  meta_description = models.TextField(null=True,blank=True ,default="")
  
  def __str__ (self):
    return self.titel