from django.urls import path  
from . import views
app_name = 'vendor_dachs'
urlpatterns = [
     path('',views.vindor_dach,name='vendor_dach'),
]