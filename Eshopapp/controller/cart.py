from django.shortcuts import render, redirect, HttpResponse
from django.http.response import JsonResponse
from django.contrib import messages
from Eshopapp.models import Product, Cart, WishList


def addtocart(request):

    if request.method == 'POST':
        if request.user.is_authenticated:
            product_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=product_id)
            if(product_check):
                if (Cart.objects.filter(user=request.user.id, product_id=product_id)):
                    return JsonResponse({'status': 'Already in Cart.'})
                else:
                    product_qty = int(request.POST.get('product_qty'))
                    if product_check.quantity >= product_qty:
                        Cart.objects.create(
                            user=request.user, product_id=product_id, product_qty=product_qty)
                        return JsonResponse({'status': 'Product added successfully.'})
                    else:
                        return JsonResponse({'status': 'Only '+str(product_check.quantity)+' quantity available.'})
            else:
                return JsonResponse({'status': 'No such product found.'})
        else:
            return JsonResponse({'status': 'Login to Continue..!!'})
    else:
        return redirect('/')


def cartview(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        context = {'cart': cart}
        return render(request, 'Eshopapp/cart/cart.html', context)
    else:
        return redirect('/')


def delete_cart_item(request):
    if request.method == 'POST':
        pord_id = request.POST.get('product_id')
        if (Cart.objects.filter(user=request.user, product__id=pord_id)):
            Cart.objects.filter(user=request.user, product__id=pord_id).delete()       
            return JsonResponse({'status':'Product removed successfully.'})                
    else:
        return redirect('/')


def update_cart(request):    
    if request.method == 'POST':
        prod_id = request.POST.get('product_id')
        print(prod_id)
        if Cart.objects.filter(user=request.user, product__id=prod_id):
            prod_qty = request.POST.get('product_qty')
            print(prod_qty)
            cart = Cart.objects.get(product__id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            
        else:
            return JsonResponse({'status':'something went wrong.'})
    return redirect('/')

