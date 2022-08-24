from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from Eshopapp.models import WishList,Product
from django.contrib.auth.decorators import login_required


def showwishlist(request):
    if request.user.is_authenticated:
        wishlist = WishList.objects.filter(user = request.user)
        context = {'wishlist': wishlist}
        return render(request, 'Eshopapp/wishlist/wishlist.html',context)
    else:
        return redirect('/')


def addtowishlist(request):    
    if request.method == 'POST':
        if request.user.is_authenticated:    
            prod_id = request.POST.get('product_id')
            product_check = Product.objects.get(id=prod_id)
            if (product_check):
                
                if  WishList.objects.filter(user=request.user, product_id=prod_id):
                    return JsonResponse({'status': 'Item already in Wishlist.'})
                else:
                    WishList.objects.create(user=request.user, product_id=prod_id)                    
                    return JsonResponse({'status': 'Item added to Wishlist.'})  
            else:
                return JsonResponse({'status':'No such product'})                  
        
        else:
            return JsonResponse({'status': 'Login to continue.'})
    else:
        return redirect('/')

def removeWishlistItem(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = request.POST.get('product_id')
            if WishList.objects.filter(user=request.user, product_id=prod_id):
                WishList.objects.filter(user=request.user, product_id=prod_id).delete()
                return JsonResponse({'status':'Item removed successfully.'})
            else:
                return JsonResponse({'status':"Somthing went wrong... Can't remove item."})                
        else:
            return redirect('/')    
    else:
        return JsonResponse({'status':'Login to continue.'})
