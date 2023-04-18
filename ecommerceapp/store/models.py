from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True) # slug is a url human friendly version of the title

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title
  
