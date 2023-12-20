from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseRedirect, HttpResponse
from .forms import *

# Create your views here.


def index(request):
    dishes = Dishes.objects.all()
    return render(request, 'index.html', context={'dishes': dishes})

def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', 'Undefined')
        category = request.POST.get('category', 'Undefined')
        price = request.POST.get('price', 'Undefined')
        ingredients = request.POST.get('ingredients', 'Undefined')
        Dishes.objects.create(name=name, category_id=category, price=price, ingredients=ingredients)

        return HttpResponseRedirect('/')
    else:
        add_dishes = AddDishes()
        return render(request, 'add.html', context={'add_dishes': add_dishes})
def edit(request):
    dishes = Dishes.objects.all()
    return render(request, 'edit.html', context={'dishes': dishes})

def delete(request):
    dishes = Dishes.objects.all()
    return render(request, 'delete.html', context={'dishes': dishes})

def edit_choose(request, id):
    try:
        if request.method == "POST":
            dishes = Dishes.objects.get(id=id)

            dishes.name = request.POST.get('name', 'Undefined')
            dishes.category_id = request.POST.get('category', 'Undefined')
            dishes.price = request.POST.get('price', 'Undefined')
            dishes.ingredients = request.POST.get('ingredients', 'Undefined')

            dishes.save()

            dishes = Dishes.objects.all()
            return render(request, 'edit.html', context={'dishes': dishes})
        else:
            dishes = Dishes.objects.get(id=id)
            form = DishesEditForm(instance=dishes)
            return render(request, 'edit_choose.html', context={'form': form})

    except Dishes.DoesNotExist:
        return HttpResponseRedirect('/')

def delete_choose(request, id):
    try:
        dishes = Dishes.objects.get(id=id)
        dishes.delete()
        dishes = Dishes.objects.all()
        return render(request, 'delete.html', {'dishes': dishes})
    except Dishes.DoesNotExist:
        dishes = Dishes.objects.all()
        return render(request, 'delete.html', {'dishes': dishes})