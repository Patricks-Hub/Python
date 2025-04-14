from django.urls import path
from . import views

urlpatterns = [
    path('', views.todo_list, name='todo_list'),
    path('add/', views.add_item, name='add_item'),
    path('toggle/<int:item_id>/', views.toggle_item, name='toggle_item'),
    path('delete/<int:item_id>/', views.delete_item, name='delete_item'),
]