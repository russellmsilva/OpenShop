from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from category.models import Category
from .forms import ProductForm
from .models import Product

# View to handle the creation of a new product
@login_required # Ensure only logged-in users can post products
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) # Create a new product instance but don't save it yet
            product.seller = request.user # Set the seller to the current user
            product.save() # Save the product instance to the database
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'products/new_product.html', {'form': form})

# View to list products alphabetically on the product gallery webpage
def product_list(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'products/product_list.html', {'products': products})

# View to remder the products detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

# View to duplicate product list template by category (so each category can have its own product list page)
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_list.html', {
        'category': category,
        'products': products
    })
