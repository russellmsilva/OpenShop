from django.contrib import admin
from .models import Category

# Register the Category model with the Django admin site
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Automatically populate the slug field based on the name
    list_display = ('name', 'slug') # Display name and slug in the admin list
