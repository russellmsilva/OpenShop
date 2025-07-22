from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True) # Unique name for the category
    slug = models.SlugField(max_length=100, unique=True) # Slug for URL-friendly representation

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
