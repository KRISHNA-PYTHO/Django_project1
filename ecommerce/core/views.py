from django.shortcuts import render, redirect
from .models import Product  
from .forms import RegistrationForm, AuthenticateForm, ChangePasswordForm, UserProfileForm, AdminProfileForm
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Home Page
def home(request):
    return render(request, 'core/home.html')

# About Page
def about(request):
    return render(request, 'core/about.html')

# Contact Page
def contact(request):
    return render(request, 'core/contact.html')

# Shampoo Category
def shampoo_categories(request):
    products = Product.objects.filter(category='SHAMPOO')
    return render(request, 'core/shampoo_categories.html', {'products': products})

# Serum Category
def serum_categories(request):
    products = Product.objects.filter(category='SERUM')
    return render(request, 'core/serum_categories.html', {'products': products})

# Hair Colour Category
def hair_categories(request):
    products = Product.objects.filter(category='HAIR_COLOUR')
    return render(request, 'core/hair_categories.html', {'products': products})

# Product Details
def product_details(request, id):
    product = Product.objects.get(pk=id)
    return render(request, 'core/product_details.html', {'product': product})


# =======================================================================================

# Registration View
def register(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegistrationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Registration Successful!')
                return redirect('register')
        else:
            form = RegistrationForm()
        return render(request, 'core/register.html', {'form': form})
    else:
        return redirect('profile')

# Login View
def log_in(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticateForm(request, request.POST)
            if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
        else:
            form = AuthenticateForm()
        return render(request, 'core/login.html', {'form': form})
    else:
        return redirect('profile')

# Profile View
def profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AdminProfileForm(request.POST, instance=request.user) if request.user.is_superuser else UserProfileForm(request.POST, instance=request.user)
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile Updated Successfully!')
        else:
            form = AdminProfileForm(instance=request.user) if request.user.is_superuser else UserProfileForm(instance=request.user)
        return render(request, 'core/profile.html', {'name': request.user, 'form': form})
    else:
        return redirect('login')

# Logout View
def log_out(request):
    logout(request)
    return redirect('home')

# Change Password View
def changepassword(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ChangePasswordForm(request.user, request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = ChangePasswordForm(request.user)
        return render(request, 'core/changepassword.html', {'form': form})
    else:
        return redirect('login')
