from django import forms
from .models import Categories, Products#, Orders


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categories
        fields = ['name', 'description', 'image_path']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'image_path': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'description', 'price', 'category', 'image_path']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'forms-select'}),
            'image_path': forms.TextInput(attrs={'class': 'form-control'})
        }
        
       
#class OrderForm(forms.ModelForm):
#    class Meta:
#        model = Orders
#        fields = ['name', 'description', 'price', 'category', 'image_path']
#        widgets = {
#            'client_name': forms.TextInput(attrs={'class': 'form-control'}),
#            'description': forms.Textarea(attrs={'class': 'form-control'}),
#            'price': forms.NumberInput(attrs={'class': 'form-control'}),
#            'category': forms.Select(attrs={'class': 'forms-select'}),
#            'image_path': forms.TextInput(attrs={'class': 'form-control'})
#        }