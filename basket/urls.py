from django.urls import path 
from . import views

app_name = 'basket'

urlpatterns = [
    path('main/', views.basket, name='basket')
]