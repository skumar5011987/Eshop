from django.shortcuts import render, redirect
from django.http.response import JsonResponse, HttpResponse
from django.contrib import messages
from Eshopapp.models import Cart, Order, OrderItems, Product, Profile
from django.contrib.auth.models import User
import random

from django.contrib.auth.decorators import login_required


@login_required(login_url='user_login')
def checkout_items(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.filter(id=item.id).delete()

    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty

    userprofile = Profile.objects.filter(user=request.user).first()

    context = {
        'cartitems': cartitems,
        'total_price': total_price,
        'userprofile': userprofile,
    }
    return render(request, 'Eshopapp/cart/checkout.html', context)


@login_required(login_url='user_login')
def placeorder(request):
    if request.method == 'POST':
        currentuser = User.objects.filter(id=request.user.id).first()
        if not currentuser.first_name:
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lname')
            currentuser.email = request.POST.get('email')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.mobile = request.POST.get('mobile')
            userprofile.address = request.POST.get('address')
            userprofile.district = request.POST.get('district')
            userprofile.state = request.POST.get('state')
            userprofile.country = request.POST.get('country')
            userprofile.pincode = request.POST.get('pincode')
            userprofile.save()

        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.mobile = request.POST.get('mobile')
        neworder.address = request.POST.get('address')
        neworder.district = request.POST.get('district')
        neworder.state = request.POST.get('state')
        neworder.country = request.POST.get('country')
        neworder.pincode = request.POST.get('pincode')
        neworder.payment_mode = request.POST.get('payment_mode')
        neworder.payment_id = request.POST.get('payment_id')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price
        trackno = 'eshop_' + str(request.user) + "_" + \
            str(random.randint(1111111111, 9999999999))

        while Order.objects.filter(tracking_no=trackno) is None:
            trackno = 'eshop_' + str(request.user) + "_" + \
                str(random.randint(11111111, 99999999))

        neworder.tracking_no = trackno
        neworder.save()
        neworderItems = Cart.objects.filter(user=request.user)
        for item in neworderItems:
            OrderItems.objects.create(
                order=neworder,
                product=item.product,
                price=item.product.selling_price,
                quantity=item.product_qty
            )

        # To update product quantity in the stockks
        orderproduct = Product.objects.filter(id=item.product.id).first()
        orderproduct.quantity = orderproduct.quantity - item.product_qty
        orderproduct.save()

        # To clear user cart items after checkout
        Cart.objects.filter(user=request.user).delete()
        # messages.success(request, 'Order placed successfully.')
        payMode = request.POST.get('payment_mode')
        if (payMode == 'Razorpay'):
            return JsonResponse({'status': 'Order placed successfully.'})

    return redirect('/')


@login_required(login_url='user_login')
def razorpaycheck(request):
    cart = Cart.objects.filter(user=request.user)
    total_cost = 0
    for item in cart:
        total_cost += item.product.selling_price * item.product_qty

    return JsonResponse({
        'total_cost': total_cost
    })


def myorders(request):
    return HttpResponse("My orders page")
