from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) # slug is a url human friendly version of the title

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
  
class Product(models.Model):
    user = models.ForeignKey(User, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/product_images/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('-created_at',)
        
    def __str__(self):
        return self.title