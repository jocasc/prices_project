from django.urls import path
from . import views

app_name = 'supermarket'

urlpatterns = [
    path('', views.product_list, name='product_list'),
]