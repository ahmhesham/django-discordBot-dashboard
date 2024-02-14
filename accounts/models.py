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
import os


# Defining a function to handle uploading avatar images for user profiles
def profile_avatar_upload_to(instance, filename):
  return f'profiles/{instance.id}/images/avatar/{filename}'


# Defining the Profile model, which represents user profiles in the application
class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='user', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to=profile_avatar_upload_to)
    bio = models.TextField(default='this is your bio you can edit it if you want.', blank=True)
    discord_id = models.BigIntegerField(null=True,blank=True)
    restricted = models.BooleanField(default=False)
    
    
   # Defining the string representation of the Profile model

    def __str__(self):
        return self.user.username

       # Overriding the save method to handle image uploads and deletions

    def save(self, *args, **kwargs):
      if self.pk is None:
        saved_image = self.avatar
        self.avatar = None
        super().save(*args, **kwargs)
        self.avatar = saved_image
        if 'force_insert' in kwargs:
          kwargs.pop('force_insert')
        super().save(*args, **kwargs)
      else:
        old_image = Profile.objects.get(pk=self.pk).avatar
        print(self.avatar)
        if self.avatar != old_image:
          if old_image == "default.jpg":
           pass
          else:
           os.remove(old_image.path)
        super().save(*args, **kwargs)










# Defining a signal to create a new Profile whenever a new User is created

def create_profile(sender , **kwargs):
    if kwargs['created']:
        new_profile = Profile.objects.create(user=kwargs['instance'])

# Connecting the create_profile signal to the User model's post_save signal

post_save.connect(create_profile, sender=User)













