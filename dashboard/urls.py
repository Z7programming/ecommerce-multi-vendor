
from django.urls import path
from .import views
app_name = 'dashboard'
urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('new-product/', views.new_product, name='new-product'),
    path('delet-product/<int:id>', views.delete_product, name='delet-product'),
    path('edit-product/<int:id>', views.edit_product, name='edit-product'),
]
