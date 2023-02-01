from django.shortcuts import render
from datetime import datetime
import requests


def product_list(request):
    username = 'joca'
    password = 'ciencia$$'
    date = datetime.now()
    base_url = f'http://joca.pythonanywhere.com/promocao/{date.day}/{date.month}/{date.year}/produto/'
    r = requests.get(f'{base_url}')
    products = r.json()
    return render(request, 'supermarket/index.html',{'products':products})
