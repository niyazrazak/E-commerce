from django.shortcuts import render
from .models import *

# Create your views here.


def store(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'store.html', context)


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = order.object.get_or_create(
            customer=customer, complete=False)
        item = order.orderitem_ser.all()
    else:
        item = []
    context = {'items': items}
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')
