from django.shortcuts import render ,redirect

# Create your views here.
from .models import Item
from .models import *

from .forms import Itemform

# create
def create_item(request):
    if request.method == 'POST':
        form = Itemform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
        # D:\myproject\Last_time_learning\Last_time_learning-\learning\myapp\templates
    else:
        form = Itemform()
    return render(request, 'myapp/item_form.html', {'form': form})
        

# read
def item_list(request):
    items = Item.objects.all()
    return render(request , 'myapp/item_list.html', {'items': items})


# update
def update_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        form = Itemform(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = Itemform(instance=item)
    return render(request, 'myapp/item_form.html', {'form': form})


def delete_item(request, pk):
    item = Item.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'myapp/item_confirm_delete.html', {'item': item})
