from django.urls import path  
from . import views
app_name='Home'
urlpatterns = [
     path('',views.store,name= 'Store'),
     path('categoreis/<int:id>',views.category_show, name='category_show'),
     path('products/<int:id>',views.products, name='products'),
     
]