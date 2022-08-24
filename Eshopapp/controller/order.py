from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from Eshopapp.models import Order, OrderItems
from django.contrib.auth.decorators import login_required


@login_required(login_url='user_login')
def index(request):
    orders = Order.objects.filter(user=request.user)
    contex = {'orders': orders}
    return render(request, 'Eshopapp/orders/index.html', contex)


def vieworder(request, t_no):
    order = Order.objects.filter(
        tracking_no=t_no).filter(user=request.user).first()
    orderitem = OrderItems.objects.filter(order=order)
    context = {'order': order, 'orderitem': orderitem}
    return render(request, 'Eshopapp/orders/vieworder.html', context)
