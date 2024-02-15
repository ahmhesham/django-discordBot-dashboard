# django-discordBot-dashboard
django-discordBot-dashboard It contains the bot and the dashboard all in one project 

this project is a simple discord bot and its dashboard in the same project using only python and html, css 

i used a really good package caled djsngo-allauth so i can handle the auth of the discord account and get the user secret_token and refresh_token its rally important so u can know what servers the user joiend and is he a admin or not 
you can find this in the code

i also crated profile to store the user avatar and discord_id you can store whatever you want using the signals. 

after this i created two views one for the main page simply it gets all the user guilds and check if the guilds in the db and if not it create guild in the db and it shows all the guilds in the mainpage all the guilds that the user have administrator role in it 

secound page is to access a specific guild with its id so u can do whatever you want to do and i'v added a good feature that if the bot is not joined to the guild it will say add the bot to your guild and its really good one and i think thats all.

 check the code every line is important
# Setup::

to setup you discord auth you will need your :

1- ``CLIENT ID`` 

2- ``CLIENT SECRET`` 

you will but it in the database using django admin panel  and you all good to go 

i hope you find this helpful thank you for reading
