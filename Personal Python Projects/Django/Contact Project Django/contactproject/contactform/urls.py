from django.urls import path
from . import views  # Import views from the same directory

urlpatterns = [
    path('', views.contact_form, name='contact_form'),
    path('success/', views.success, name='success'),
]