from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from .models import User
from django import forms
from django.utils.translation import gettext, gettext_lazy as _

class RegistrationForm(UserCreationForm):
    password1 = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control bg-light', 'placeholder': 'Enter password'}))
    password2 = forms.CharField(label=_('Confirm Password'),strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control bg-light', 'placeholder': 'Enter password'}))

    class Meta:
        model=User
        fields = ['username','email','password1','password2']
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter username'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder': 'Enter e-mail'}),            
        }
        labels={
            'email':'Email',
            'password1':'Password',
            'password2':'Confirm Password'
        }

class CustomUserLogin(AuthenticationForm):
    username = UsernameField(label=_('Username'), strip=False,widget=forms.TextInput(
        attrs={'class':'form-control bg-light','placeholder':'Enter username'}))
    password = forms.CharField(label=_('Password'), strip=False, widget=forms.PasswordInput(
        attrs={'autocomplete': 'current-password', 'class': 'form-control bg-light', 'placeholder': 'Enter password'}))
