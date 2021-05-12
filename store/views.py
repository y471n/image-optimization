from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.conf import settings

def index(request):
    return HttpResponse('Hello')


def store(request):
    products = Product.objects.all()
    context = {'products': products, 'MEDIA_CDN': settings.MEDIA_CDN}
    return render(request, 'store/store.html', context)


def cart(request):
    context = {}
    return render(request, 'store/cart.html')


def checkout(request):
    context = {}
    return render(request, 'store/checkout.html')
