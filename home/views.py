from django.shortcuts import render
from category.models import Category

def homepage(request):
    return render(request, 'home.html')
