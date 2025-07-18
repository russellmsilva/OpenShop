from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'), # Page for listing general products
    path('new/', views.new_product, name='new_product'), # Page for creating a new product not already listed
]
