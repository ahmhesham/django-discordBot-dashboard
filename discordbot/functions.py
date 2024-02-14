
from django.shortcuts import render , HttpResponse
import  requests
from django.contrib.auth import logout
from .models import *
from django.shortcuts import redirect
# Create your views here.
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
from sitev.settings import API_ENDPOINT ,CLIENT_ID  ,CLIENT_SECRET ,REFRESH_TOKEN ,REDIRECT_URI
from .classes import *
from django.core.exceptions import ObjectDoesNotExist


social_token = social_token_class()


def refresh_token(refresh_token):
  data = {
    'grant_type': 'refresh_token',
    'refresh_token': social_token.token_secret()
  }
  headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
  }
  r = requests.post(API_ENDPOINT, data=data, headers=headers, auth=(CLIENT_ID, CLIENT_SECRET))
  r.raise_for_status()
  return r.json()






def is_bot_in_guild(guild_id):
    url = f"https://discord.com/api/v10/guilds/{guild_id}"
    headers = {
        "Authorization": f"Bot token",
        "Content-Type": "application/json"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Bot is in the guild
        return True
    elif response.status_code == 404:
        # Bot is not in the guild
        return False
    



def get_owner_id(guild_id):
    url = "https://discord.com/api/v10/guilds/{guild_id}"
    headers = {
        "Authorization": "Bot token",
        "Content-Type": "application/json"
        }
    response = requests.get(url.format(guild_id=guild_id), headers=headers)
    
    owner_id = response.json()["owner_id"]
    print(owner_id)
    return owner_id

def get_gulids(token, request):
    response = requests.get("https://discord.com/api/v10/users/@me/guilds", headers={
        'Authorization': 'Bearer %s' % token
        })
    if response.status_code == 200:
        guilds = []
        for guild in response.json():
            if guild['owner'] or (int(guild['permissions']) & 0x8) == 0x8:
                guilds.append(guild)
        return guilds
    else:
        print("The token is invalid.")
        #return login_agin so i can use it to mke him logout and then update the  code 
        return 'login_agin'
    


def my_guildss(request):
    token = social_token.token(uid=request.user.id)
    #get all the guilds 
    user_id = request.user.id 
    token_secrett = social_token.token(uid=user_id)
    guilds_api = get_gulids(token=token_secrett, request=request)
    if guilds_api == 'login_agin':
        logout(request)
        return redirect('account_login')
    else:
        #print(guilds_api)
        ids_list = [int(d['id']) for d in guilds_api]
        #print(ids_list)
        #get the guilds in the  database
        profile = Profile.objects.get(user=request.user)
        for guild_id in ids_list:
            try:
                guild = Guild.objects.get(guild_id=guild_id)
            except ObjectDoesNotExist:
                for guildd in guilds_api:
                    if guildd['id'] == f'{guild_id}':
                        guild_id_to_db = guildd['id']
                        guild_name = guildd['name']
                        guild_icon_code = guildd['icon']
                        if guild_icon_code == None:
                            guild_icon = None
                        else:
                            guild_icon = f"https://cdn.discordapp.com/icons/{guild_id_to_db}/{guild_icon_code}.png"
                        owner = guildd['owner']
                        if owner == True:
                            owner_id = profile.discord_id
                            Guild.objects.create(
                                guild_id=guild_id_to_db,
                                guild_name=guild_name,
                                guild_icon=guild_icon,
                                guild_owner_id=owner_id,
                            )
                            print('created')
                        else:
                            bot_joined = is_bot_in_guild(guild_id=guild_id_to_db)
                            if bot_joined == True:
                                owner_id = get_owner_id(guild_id=guild_id_to_db)
                            else:
                                owner_id = None
                            Guild.objects.create(
                                guild_id=guild_id_to_db,
                                guild_name=guild_name,
                                guild_icon=guild_icon,
                                guild_owner_id=owner_id,
                            )
                            print('created not the owner owner')
            else:
                # Guild exists
                guilds = Guild.objects.filter(guild_id__in=ids_list)
                for guildd in guilds_api:
                    guild_id_to_db = guildd['id']
                    guild_name = guildd['name']
                    guild_icon_code = guildd['icon']
                    if guild_icon_code is None:
                        guild_icon = None
                    else:
                        guild_icon = f"https://cdn.discordapp.com/icons/{guild_id_to_db}/{guild_icon_code}.png"
                        owner = guildd['owner']
                        if owner == True:
                            owner_id = profile.discord_id
                        else:
                            bot_joined = is_bot_in_guild(guild_id=guild_id_to_db)
                            if bot_joined == True:
                                owner_id = get_owner_id(guild_id=guild_id_to_db)
                            else:
                                owner_id = None
                    gupdate, _ = Guild.objects.update_or_create(
                        guild_id=guild_id_to_db,
                        defaults={
                            'guild_name': guild_name,
                            'guild_icon': guild_icon,
                            'guild_owner_id': owner_id,
                        }
                    )
                    # Save the updated guild information
                    gupdate.save()
            
                
        guilds = Guild.objects.filter(guild_id__in=ids_list)
        #print(guilds)

        contx = {
            'guilds':guilds,
            'user': request.user,
        }
        return guilds