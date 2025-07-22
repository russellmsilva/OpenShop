from django import forms
from .models import ShippingAddress

class ShippingAddressForm(forms.ModelForm):
    class Meta:
        model = ShippingAddress
        fields = ['full_name', 'street_address', 'city', 'postal_code', 'country', 'phone_number']

    def clean_postal_code(self):
        code = self.cleaned_data.get('postal_code')
        if not code.isalnum():
            raise forms.ValidationError("Postal code must be alphanumeric.")
        return code

    def clean_phone_number(self):
        phone = self.cleaned_data.get('phone_number')
        country = self.cleaned_data.get('country')
        if country == "US" and not phone:
            raise forms.ValidationError("Phone number is required for U.S. addresses.")
        return phone
