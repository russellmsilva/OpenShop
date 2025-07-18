from django.db import models
from django.contrib.auth.models import User

# Each product has an associated user (Products to Users represent a many to one relationship)
# as well as a name, description, and associated image
class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return self.name
