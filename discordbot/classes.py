
from django.shortcuts import render , HttpResponse
import  requests
from .models import *
# Create your views here.
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
from sitev.settings import API_ENDPOINT ,CLIENT_ID  ,CLIENT_SECRET ,REFRESH_TOKEN ,REDIRECT_URI



class social_token_class():
    def token(self, uid):
        social_token = SocialToken.objects.get(account__user=uid)
        return social_token.token
    def token_secret(self, uid):
        social_token = SocialToken.objects.get(account__user=uid)
        return social_token.token_secret
    
social_token = social_token_class()

