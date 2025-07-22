from django.urls import path
from . import views

urlpatterns = [
    path('', views.manage_shipping_address, name='manage_shipping')
]
