from django.shortcuts import render

from .models import Category, Product

def category_detail(request, slug):
    category = Category.objects.get(slug=slug)
    products = category.products.all()
    return render(request, 'store/category_detail.html',
                   {'category': category,
                    'products': products})

def product_detail(request, category_slug, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'store/product_detail.html',
                   {'product': product})
