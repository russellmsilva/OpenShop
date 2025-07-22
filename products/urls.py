from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='products'), # Page for listing general products
    path('new/', views.new_product, name='new_product'), # Page for creating a new product not already listed
    path('<int:pk>/', views.product_detail, name='product_detail'),  # Dynamically generated page for each product based on its primary key
    path('category/<slug:slug>/', views.category_products, name='category_products'), # Page for listing products by category, using the slug to identify the category
]
