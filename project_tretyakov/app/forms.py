from django import forms
from .models import *

class AddDishes(forms.Form):
    name = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'name': 'name'}))
    category = forms.ChoiceField(required=True, label='', choices=((1, 'Супы'), (2, 'Горячее'), (3, 'Холодное'),
                                                                   (4, 'Салаты'), (5, 'Морепродукты')), widget=forms.Select(attrs={'category': 'category'}))
    price = forms.CharField(required=True, label='', widget=forms.TextInput(attrs={'price': 'price'}))
    ingredients = forms.CharField(required=True, label='', widget=forms.Textarea(attrs={'ingredients': 'ingredients'}))

class DishesEditForm(forms.ModelForm):
    class Meta:
        model = Dishes
        fields = '__all__'
