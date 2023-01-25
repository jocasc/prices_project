from django.shortcuts import render
import requests


def product_list(request):
    username = 'joca'
    password = 'ciencia$$'
    base_url = 'http://joca.pythonanywhere.com/produtos/'
    r = requests.get(f'{base_url}')
    products = r.json()
    return render(request, 'supermarket/index.html',{'products':products})
