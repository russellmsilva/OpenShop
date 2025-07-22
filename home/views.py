from django.shortcuts import render
from django.http import HttpResponse
from category.models import Category

def homepage(request):
    categories = Category.objects.all().order_by('name')
    return render(request, 'home.html', {'categories': categories})
