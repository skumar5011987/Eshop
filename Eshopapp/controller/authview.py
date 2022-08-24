from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from Eshopapp.forms import *
from django.contrib import messages
from django.contrib.auth.models import Group


def user_registeration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful.')
            return redirect('user_registration')
    else:
        form = RegistrationForm()
    context = {'form': form}
    return render(request, 'Eshopapp/auth/register.html', context)


def user_login(request):
    if request.user.is_authenticated:
        messages.warning(request, 'Already Logged in.')
        return redirect('/')
    if request.method == 'POST':
        if request.POST['username'] == "" or request.POST['password'] == "":
            messages.error(request, 'Username or password is Blank.')
            return redirect('user_login')
        form = CustomUserLogin(request=request, data=request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            upass = form.cleaned_data['password']
            user = authenticate(username=uname, password=upass)
            if user is not None:
                login(request, user)
                messages.success(request, 'Logged in successfully.')
                return redirect('/')
        else:
            messages.error(
                request, 'Username or password is incorrect. Note that, both fields may be case sensitive.')
            return redirect('user_login')
    else:
        form = CustomUserLogin()
    context = {'form': form}
    return render(request, 'Eshopapp/auth/login.html', context)


def user_logout(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Suspicious activity detected.')

    else:
        logout(request)
        messages.success(request, 'Logged out successfully.')
    return redirect('/')
