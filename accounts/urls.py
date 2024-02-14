from django import views
from django.urls import path

from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
