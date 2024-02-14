from django.shortcuts import render , HttpResponse, redirect
import  requests
from .models import *
# Create your views here.
from django.contrib.auth import logout
from allauth.socialaccount.models import SocialToken
from django.contrib.auth.decorators import login_required
from sitev.settings import API_ENDPOINT ,CLIENT_ID  ,CLIENT_SECRET ,REFRESH_TOKEN ,REDIRECT_URI
from .classes import social_token_class
from .functions import get_gulids,get_owner_id,is_bot_in_guild,my_guildss
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages


social_token = social_token_class()




@login_required
def my_guilds(request):
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
        return render(request, 'dashboard.html', context=contx)
    




@login_required
def guild(request, gid):
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
        
        guild = Guild.objects.get(guild_id=gid)
        guild_id = guild.guild_id
        if guild_id in ids_list:
            bot_joined = is_bot_in_guild(guild_id=guild_id)
            if bot_joined == True:
                joined= True
            else:
                joined = False
            contx = {
                'joined':joined,
                'guild':guild,
                'guilds':guilds,
                'user': request.user,
                }
            return render(request, 'guilds/guild_page.html', context=contx)
        else:
            messages.error(request, "You Don't Have permissons in this guild to access its data")
            return redirect('dashboard')
