import email
from re import T
from django.db import models
from django.shortcuts import render , HttpResponse , get_object_or_404, HttpResponseRedirect
# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

from django.template.defaultfilters import slugify
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

from accounts.models import *



class Guild(models.Model):
    guild_id = models.BigIntegerField(null=True,blank=True)
    guild_name = models.CharField(max_length=200,null=True,blank=True)
    guild_icon = models.CharField(max_length=2000,null=True,blank=True)
    guild_owner_id = models.BigIntegerField(null=True,blank=True)


    def __str__(self):
        return self.guild_name + ' ' + '||'+ ' ' + str(self.guild_id)

