from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from category.models import Category
from cart.forms import AddToCartForm
from cart.models import CartItem
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

# View to render the products detail page
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    # Check if the user is not trying to add their own product to the cart
    error_message = None
    if product.seller == request.user:
        error_message = "You can't add your own product to the cart."

    # Check if the user is authenticated before allowing them to add to cart
    if not request.user.is_authenticated:
        error_message = "You must be logged in to add products to the cart."

    form = AddToCartForm(request.POST or None)
    if request.method == 'POST' and form.is_valid() and not error_message:
        existing_item = CartItem.objects.filter(
            buyer=request.user,
            product=product
        ).first()

        # If the product is an existing item, just update the quantity, do not create a new product entry in the cart
        if existing_item:
            existing_item.quantity += form.cleaned_data['quantity']
            existing_item.save()
        else:
            CartItem.objects.create(
                buyer=request.user,
                product=product,
                quantity=form.cleaned_data['quantity']
            )

        return redirect('display_cart')

    return render(request, 'products/product_detail.html', {
        'product': product,
        'form': form,
        'error_message': error_message
    })

# View to duplicate product list template by category (so each category can have its own product list page)
def category_products(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Product.objects.filter(category=category)
    return render(request, 'products/category_list.html', {
        'category': category,
        'products': products
    })
