from django.urls import path
from . import views

urlpatterns = [
    path('', views.filament_calculator, name='filament_calculator'),
]