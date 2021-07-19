from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import *
from .models import Item

# Create your views here.
def home(request):
    items = Item.objects.all()
    return render(request, 'home.html', {'items' : items})

def detail(request):
    return render(request, 'detail.html')

def create(request):
    if request.method == 'POST':
        new_item = Item()
        new_item.name = request.POST['name']
        new_item.price = request.POST['price']
        new_item.image = request.FILES['image']
        new_item.body = request.POST['body']
        new_item.save() 
        return redirect('home')
    else:
        return render(request, 'new.html')

def detail(request, id):
    item = get_object_or_404(Item, pk=id)
    return render(request, 'detail.html', {'item' : item})

def update(request, id):
    if request.method == 'POST':
        update_item = Item.objects.get(id = id)
        update_item.name = request.POST['name']
        update_item.price = request.POST['price']
        update_item.image = request.FILES['image']
        update_item.body = request.POST['body']
        update_item.save()
        return redirect('detail', update_item.id)
    else:
        item = Item.objects.get(id = id)
        return render(request, 'edit.html', {'item':item})
        
def delete(request, id):
    delete_item = Item.objects.get(id = id)
    delete_item.delete()
    return redirect('home')