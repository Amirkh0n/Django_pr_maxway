from django.urls import path
from .views import *


urlpatterns = [
    # authentication pages
    path('login/', login_page, name='login_page'),
    path('logout_page/', logout_page, name='logout_page'),
    
    # categories pages
    path('categories/', categories_view, name='categories_page' ),
    path('categories/create/', category_create_view, name='category_create'),
    path('categories/<int:pk>/edit/', category_edit_view, name='category_edit'),
    path('categories/<int:pk>/delete/', category_delete_view, name='category_delete'),
    
    # products pages
    path('products/', products_view, name='products_page' ),
    path('products/create/', product_create_view, name='product_create'),
    path('products/<int:pk>/edit/', product_edit_view, name='product_edit'),
    path('products/<int:pk>/delete/', product_delete_view, name='product_delete'),
    
    # products pages
    path('orders/', orders_view, name='orders_page' ),
    path('orders/create/', product_create_view, name='product_create'),
    path('orders/<int:pk>/edit/', product_edit_view, name='product_edit'),
    path('orders/<int:pk>/delete/', product_delete_view, name='product_delete'),
    
    # dashboard page
    path('', index_view, name='dashboard'),
]