from distutils.command.build_scripts import first_line_re
import email
from django.shortcuts import render , HttpResponse
from django.contrib.auth.forms import UserCreationForm , UserChangeForm 
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms 
from .models import *
from django.utils.safestring import mark_safe
from django.contrib.auth.forms import AuthenticationForm
from captcha.fields import ReCaptchaField
from allauth.account.forms import LoginForm



class SignUpForm(UserCreationForm, ):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.error_messages = {
            'username_match': 'username is already exist',
            'email_match': 'Email is already exist',
            'password_mismatch': 'these two password isn\'t match try again'
        }

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(self.error_messages['email_match'],)
        return email
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=150)
    
    captcha = ReCaptchaField()
    
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'captcha')
        help_texts = {
            'password1': None,
            'password2': None,
            'email': None,
            
        }
        

class MyLoginForm(LoginForm):

    def __init__(self, *args, **kwargs):
        super(MyLoginForm, self).__init__(*args, **kwargs)
        ## here u add the new fields that u need


