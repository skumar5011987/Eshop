from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from .models import Category, Product
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'Eshopapp/home.html')


def collections(request):
    category = Category.objects.filter(status=0)
    context = {'category': category}
    return render(request, 'Eshopapp/collections.html', context)


def collectionsview(request, slug):
    if (Category.objects.filter(slug=slug)):
        products = Product.objects.filter(category__slug=slug)
        category = Category.objects.filter(slug=slug).first()
        context = {'products': products, 'category': category}
        return render(request, 'Eshopapp/products/index.html', context)
    else:
        messages.warning(request, 'No product found for this Category.')
        return HttpResponseRedirect('/collections/')


def productview(request, cate_slug, prod_slug):
    if Category.objects.filter(slug=cate_slug, status=0):
        if Product.objects.filter(slug=prod_slug, status=0):
            products = Product.objects.filter(slug=prod_slug, status=0).first()
            context = {'products': products}
        else:
            messages.warning(request, 'No product found.')
            return HttpResponseRedirect('/collections/')
    else:
        messages.warning(request, 'No product found.')
        return redirect('collections')
    return render(request, 'Eshopapp/products/view.html', context)


def productlist(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    listofproduct = list(products)

    return JsonResponse(listofproduct, safe=False)
