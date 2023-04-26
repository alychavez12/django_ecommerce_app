from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, Product
from .cart import Cart


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


def add_to_cart(request, product_id):
    cart = Cart(request)
    cart.add(product_id)
    return redirect("cart_view")

def change_quantity(request, product_id):
    action = request.GET.get('action', '')

    if action:
        quantity = 1
    

    if action == "decrease":
        quantity = -1
   
    
    cart = Cart(request)
    cart.add(product_id, quantity, True)
    print (action)
    return redirect("cart_view")


def remove_from_cart(request, product_id):
    cart = Cart(request)
    cart.remove(product_id)
    return redirect("cart_view")


def cart_view(request):
    cart = Cart(request)
    return render(request, 'store/cart_view.html', {'cart': cart})

@login_required
def checkout(request):
    cart = Cart(request)
    return render(request, 'store/checkout.html', {'cart': cart})
