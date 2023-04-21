from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

from store.forms import ProductForm
from store.models import Product, Category

@login_required
def my_store(request):
    return render(request, 'userprofile/my_store.html')

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








