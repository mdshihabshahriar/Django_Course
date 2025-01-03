from django import forms
from .models import Author,Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'