import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import json
import os
import datetime
import traceback
import urllib.request, json
#tijd = int(time.strftime("%M"))
#tijd1 = str(time.strftime("%c"))
#tijd1 = datetime.datetime.now().strftime("%c")
cp = '$'
bot = commands.Bot(command_prefix=cp)

print ('Bot is aan het laden...')
print ('.....')
print ('Het laden is bijna compleet!')
print ('Bij errors exit invoeren in console!')
print ('De command prefix die wordt gebruikt is ' + cp)
print ('...')
print ('...')
print ('We zijn er bijna!')
print ('Ter info! De bot is niet bedoeld als U-bot maar als Discord Bot')
print ('Versie 1.3')
print ('Nieuwe logo en naam')
@bot.event
async def on_ready():
    await bot.edit_profile(username="HabGrab")
    bot.remove_command("help")
    #await bot.change_presence(game=discord.Game(name='Use {}help | Aardappelen'.format(cp)))
    print('Bot is geladen als')
    print(bot.user.name)
    print(bot.user.id)
	
    
	
@bot.command(pass_context = True)
async def grab(ctx, habbo):
	try:
		with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
			data = json.loads(url.read().decode())
			naamio = data['name']
			motto = data['motto']
			lidsince = data['memberSince']
			status = data['profileVisible']
			if status == True:
				status = ("De gebruiker is zichtbaar")
			else:
				status = ("De gebruiker is onzichtbaar")
				
			embed=discord.Embed(title="Hier zijn de gegevens van de opgevraagde Habbo: ", color=0xdee236)
			embed.set_thumbnail(url="http://justcakenl.tk/host/events.gif")
			embed.add_field(name="Naam:" , value=naamio, inline=True)
			embed.add_field(name="Motto:", value=motto, inline=True)
			embed.add_field(name="Lid sinds:" , value=lidsince, inline=True)
			embed.add_field(name="Zichtbaarheid:" , value=status, inline=True)
			embed.set_footer(text="Made by Mohagames205")
			await bot.say(embed=embed)
	except:
		embed=discord.Embed(title="Er is iets misgelopen", description="De gebruiker bestaat niet", color=0xe2da36)
		embed.set_thumbnail(url="http://justcakenl.tk/host/events.gif")
		embed.set_footer(text="Made by Mohagames205")
		await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def help(ctx):
	embed=discord.Embed(title="Help", description="Hier zie je alle botcommands", color=0xffff00)
	embed.add_field(name="$grab", value="Zoekt gebruikers op op Habbo", inline=True)
	embed.set_footer(text="Made by Mohagames205")
	await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))