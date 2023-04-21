from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify

from store.forms import ProductForm
from store.models import Product


@login_required
def my_store(request):
    return render(request, 'userprofile/my_store.html')

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            title = request.POST.get('title')
            slug = slugify(title)
            product = form.save(commit=False)
            product.user = request.user
            product.slug = slugify(title)
            product.save()
            return redirect('my_store')
    else:
        form = ProductForm()   
    return render(request, 'userprofile/add_product.html', {
        'form': form,
        'title': 'Add Product',
    }) 

@login_required
def edit_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('my_store')
    else:
        form = ProductForm(instance=product)
    return render(request, 'userprofile/edit_product.html', {
        'form': form,
        'title': 'Edit Product',
    })
    
@login_required
def delete_product(request, pk):
    product = Product.objects.filter(user=request.user).get(pk=pk)
    product.delete()
    return redirect('my_store')       


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('frontpage')
    else:
        error_message = "Invalid signup - try again"
        form = UserCreationForm()
        context = {'form': form, 'error_message': error_message}
        return render(request, 'userprofile/signup.html', context)








