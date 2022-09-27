from django.urls import path
from . import views
app_name = 'Home'
urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product/<str:slug>', views.product, name='product'),

]


"""
home.html
shop.html
card.html
blog.html
about.html
contact.html  

    path('card/', views.card, name='card'),
    path('blog/', views.blog, name='blog'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('categoreis/<int:id>', views.category_show, name='category_show'),
"""
