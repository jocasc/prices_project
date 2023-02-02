from django.shortcuts import render
from datetime import datetime, timedelta
import requests


def product_list(request):
    username = 'joca'
    password = 'ciencia$$'
    today = datetime.now()
    products = []
    count = 1
    while len(products) == 0:
        base_url = f'http://joca.pythonanywhere.com/promocao/{today.day}/{today.month}/{today.year}/produto/'
        r = requests.get(f'{base_url}')
        products = r.json()
        date_found = today
        count += 1
        today = today - timedelta(1)

    # date = datetime.now()
    # base_url = f'http://joca.pythonanywhere.com/promocao/{date.day}/{date.month}/{date.year}/produto/'
    # r = requests.get(f'{base_url}')
    # products = r.json()
    return render(request, 'supermarket/index.html',{'products':products, 'date_found': date_found})
