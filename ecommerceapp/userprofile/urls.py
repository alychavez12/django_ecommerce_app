from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='userprofile/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my_store/', views.my_store, name='my_store'),
    path('my_store/add_product/', views.add_product, name='add_product'),
    path('my_store/edit_product/<int:pk>/', views.edit_product, name='edit_product'),
    path('my_store/delete_product/<int:pk>/', views.delete_product, name='delete_product'),
    
]