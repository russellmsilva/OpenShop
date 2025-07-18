from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProductForm
from .models import Product

# View to handle the creation of a new product
@login_required # Ensure only logged-in users can post products
def new_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False) # Create a new product instance but don't save it yet
            product.owner = request.user # Set the owner to the current user
            product.save() # Save the product instance to the database
            return redirect('products')
    else:
        form = ProductForm()
    return render(request, 'new_product.html', {'form': form})

# View to list products alphabetically on the product gallery webpage
def product_list(request):
    products = Product.objects.all().order_by('name')
    return render(request, 'product_list.html', {'products': products})
