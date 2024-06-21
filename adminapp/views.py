from django.shortcuts import render,redirect, get_object_or_404 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
#from django.views import View
from .models import Categories, Products, Order, Customer
from .forms import CategoryForm, ProductForm#, OrderForm
#from . import services


def login_required_decorator(func):
    return login_required(func,login_url='login_page')
    

@login_required_decorator
def logout_page(request):
    logout(request)
    return redirect("login_page")


def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, password=password, username=username)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
    return render(request, 'adminapp/sign_in.html')


@login_required_decorator
def index_view(request):
    user = request.user
    count = (
        {'name': 'Categories', 'count': len(Categories.objects.all()), 'url': 'categories/'},
        {'name': 'Products', 'count': len(Products.objects.all()), 'url': 'products/' },
        {'name': 'Customers', 'count': len(Customer.objects.all()), 'url': 'customer/' },
        {'name': 'Orders', 'count': len(Order.objects.all()), 'url': 'orders/' },
    )
    return render(request, 'adminapp/index.html', {
        'username': user.username, 
        'counter': count, 
        'profile_picture': user.profile.picture.url if hasattr(user, 'profile') and user.profile.picture else None
    })


@login_required_decorator
def categories_view(request):
    user = request.user
    categories = Categories.objects.all()
    
    return render(request, 'adminapp/categories/detail.html', {'categories' : categories })


@login_required_decorator
def category_edit_view(request, pk):
    user = request.user
    category = get_object_or_404(Categories, pk = pk)
    
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories_page')
    else:
        form = CategoryForm(instance=category)
    return render(request, 'adminapp/categories/edit.html', {'forms': form})


@login_required_decorator
def category_delete_view(request, pk):
    user = request.user
    category = get_object_or_404(Categories, pk = pk)
    
    if request.method == 'POST':
        category.delete()
        return redirect('categories_page')
    return render(request, 'adminapp/categories/delete.html', {'category': category})


@login_required_decorator
def category_create_view(request):
    user = request.user
    
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories_page')
    else:
        form = CategoryForm()
    return render(request, 'adminapp/categories/edit.html', {'forms': form})


@login_required_decorator
def products_view(request):
    user = request.user
    products = Products.objects.all()
    categories = Categories.objects.all()
    
    return render(request, 'adminapp/products/detail.html', {'products' : products, 'categories' : categories })

@login_required_decorator
def product_edit_view(request, pk):
    user = request.user
    product = get_object_or_404(Products, pk = pk)
    
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    else:
        form = ProductForm(instance=product)
    return render(request, 'adminapp/products/edit.html', {'forms': form})


@login_required_decorator
def product_delete_view(request, pk):
    user = request.user
    product = get_object_or_404(Products, pk = pk)
    
    if request.method == 'POST':
        category.delete()
        return redirect('products_page')
    return render(request, 'adminapp/products/delete.html', {'product': product})


@login_required_decorator
def product_create_view(request):
    user = request.user
    
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products_page')
    else:
        form = ProductForm()
    return render(request, 'adminapp/products/edit.html', {'forms': form})

###
@login_required_decorator
def orders_view(request):
    user = request.user
    orders = Order.objects.all()
    
    return render(request, 'adminapp/products/detail.html', {'orders' : orders })

#@login_required_decorator
#def order_edit_view(request, pk):
#    user = request.user
#    order = get_object_or_404(Orders, pk = pk)
#    
#    if request.method == 'POST':
#        form = OrderForm(request.POST, instance=order)
#        if form.is_valid():
#            form.save()
#            return redirect('orders_page')
#    else:
#        form = OrderForm(instance=order)
#    return render(request, 'adminapp/products/edit.html', {'forms': form})


#@login_required_decorator
#def order_delete_view(request, pk):
#    user = request.user
#    order = get_object_or_404(Orders, pk = pk)
#    
#    if request.method == 'POST':
#        category.delete()
#        return redirect('orders_page')
#    return render(request, 'adminapp/products/delete.html', {'order': order})


#@login_required_decorator
#def order_create_view(request):
#    user = request.user
#    
#    if request.method == 'POST':
#        form = OrderForm(request.POST)
#        if form.is_valid():
#            form.save()
#            return redirect('orders_page')
#    else:
#        form = OrderForm()
#    return render(request, 'adminapp/products/edit.html', {'forms': form})

