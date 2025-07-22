from django.shortcuts import render, redirect, get_object_or_404
from .forms import ShippingAddressForm
from .models import ShippingAddress

def manage_shipping_address(request):
    address = ShippingAddress.objects.filter(user=request.user).first() # Get the user's shipping address if it exists
    if request.method == 'POST':
        form = ShippingAddressForm(request.POST, instance=address) # Bind the form with the POST data and the existing address instance
        if form.is_valid():
            shipping = form.save(commit=False)
            shipping.user = request.user
            shipping.save()
            return redirect('profile')
    else:
        form = ShippingAddressForm(instance=address)

    return render(request, 'shipping/shipping_form.html', {'form': form})
