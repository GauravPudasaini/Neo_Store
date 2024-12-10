from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LogoutView
from django.urls import reverse
from item.models import Category, Item
from django.contrib.auth.decorators import login_required
from .forms import SignupForm

def index(request):
    """
    Renders the homepage with available categories and the latest unsold items.
    """
    items = Item.objects.filter(is_sold=False)[:6]
    categories = Category.objects.all()

    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    """
    Renders the contact page.
    """
    return render(request, 'core/contact.html')

def signup(request):
    """
    Handles user signup with validation and redirects to the login page upon success.
    """
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Use the named URL 'login'
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def user_logout(request):
    """
    Logs out the user and redirects to the homepage.
    """
    logout(request)  # Log the user out
    return redirect('core:logout')

