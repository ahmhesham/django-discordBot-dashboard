import requests
from allauth.socialaccount.models import SocialAccount
from .models import *
from django.dispatch import receiver

from django.dispatch import receiver
from allauth.socialaccount.signals import social_account_added
from discordbot.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount
from allauth.socialaccount.models import SocialToken
from datetime import datetime
from django.core.files.base import ContentFile
import os

import requests
from io import BytesIO
from django.core.files.base import ContentFile
import filecmp

def is_same_image(image_path1, image_path2):
    return filecmp.cmp(image_path1, image_path2)

@receiver(post_save, sender=SocialAccount)
def social_account_saved(sender, instance, created, **kwargs):
    current_date_time = datetime.now()
    
    print(instance.extra_data)
    if created:
        #update profile and update the user profile avatar 
        uid = instance.uid
        if instance.provider == "discord":
          

          avatar = instance.extra_data['avatar']
          global_name = instance.extra_data['global_name']

          print(instance.provider)


          profile =  get_object_or_404(Profile, user=instance.user)
          image_link = f'https://cdn.discordapp.com/avatars/{instance.uid}/{avatar}.webp'

          # Download the image from the URL
          response = requests.get(image_link)
          if response.status_code != 200:
            return "Sorry, the image could not be downloaded. Please check the URL and try again."
          else:

            image_content = ContentFile(response.content)
            profile.avatar.save(f'{global_name}_avatar{instance.id}.jpg', image_content, save=True)
          profile.discord_id = instance.uid
          profile.save()
         
          dicord_profile_icon = f'https://cdn.discordapp.com/avatars/{instance.uid}/{avatar}.webp'
          

        else:
          
          print("the provider is not discord.")

    else:
      
      social_token = SocialToken.objects.get(account__user=instance.user)
      #update the user data

      profile =  get_object_or_404(Profile, user=instance.user)
      avatar = instance.extra_data['avatar']
      global_name = instance.extra_data['global_name']
      print(instance.provider)

      #update discord user data

      dicord_profile_icon = f'https://cdn.discordapp.com/avatars/{instance.uid}/{avatar}.webp'
      

      #update profile avatar

      image_link = f'https://cdn.discordapp.com/avatars/{instance.uid}/{avatar}.webp'
      print(image_link)

      # Download the image from the URL
      profile.discord_id = instance.uid
      profile.save()
      response = requests.get(image_link)
      if response.status_code != 200:

        return "Sorry, the image could not be downloaded. Please check the URL and try again."
      
      else:

        image_content = ContentFile(response.content)
        profile.avatar.save(f'{global_name}_avatar{instance.id}.jpg', image_content, save=True)
      

      print("update the user data")
       


