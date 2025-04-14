from django.shortcuts import render, redirect
from .models import TodoItem

def todo_list(request):
    items = TodoItem.objects.all()
    return render(request, 'todoapp/todo_list.html', {'items': items})

def add_item(request):
    if request.method == 'POST':
        content = request.POST['content']
        TodoItem.objects.create(content=content)
    return redirect('todo_list')

def toggle_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.completed = not item.completed
    item.save()
    return redirect('todo_list')

def delete_item(request, item_id):
    item = TodoItem.objects.get(pk=item_id)
    item.delete()
    return redirect('todo_list')