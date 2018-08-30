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
import urllib

cp = '$'
bot = commands.Bot(command_prefix=cp)
bot.remove_command("help")
print ('Bot is aan het laden...')

@bot.event
async def on_ready():
    await bot.edit_profile(username="HabGrab")
    await bot.change_presence(game=discord.Game(name='Use {}help | HabGrab ©'.format(cp)))
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
				
			if motto == "":
				motto = ("Geen")
			else:
				motto = motto
			
			urllib.request.urlretrieve(f"https://www.habbo.nl/habbo-imaging/avatarimage?hb=image&user={habbo}", "gabbo.jpg")
			embed=discord.Embed(title="Hier zijn de gegevens van de opgevraagde Habbo: ", color=0xffff00)
			embed.set_thumbnail(url="http://justcakenl.tk/host/events.gif")
			embed.add_field(name="Naam:" , value=naamio, inline=True)
			embed.add_field(name="Motto:", value=motto, inline=True)
			embed.add_field(name="Lid sinds:" , value=lidsince, inline=True)
			embed.add_field(name="Zichtbaarheid:" , value=status, inline=True)
			embed.set_image(url="./gabbo.jpg")
			embed.set_footer(text="Powered by HabGrab ©")
			channel = ctx.message.channel
			await bot.say(embed=embed)
			print("Foto verzonden")
			await bot.send_file(channel, "gabbo.jpg", content="Avatar:", filename="gabbo.jpg")
	except:
		embed=discord.Embed(title="Er is iets misgelopen", description="De gebruiker bestaat niet", color=0xffff00)
		print("Error")
		embed.set_thumbnail(url="http://justcakenl.tk/host/events.gif")
		embed.set_footer(text="Powered by HabGrab ©")
		await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def info(ctx):
	embed=discord.Embed(title="HabGrab info", description="Alle informatie die je zou willen weten over HabGrab", color=0xffff00)
	embed.set_thumbnail(url="http://justcakenl.tk/host/events.gif")
	embed.add_field(name="Creator", value="Deze discord bot is gemaakt door @Mohagames#7389", inline=False)
	embed.add_field(name="Programmeertaal", value="Discord.py 0.16.12", inline=False)
	embed.add_field(name="Githubpagina", value="https://github.com/Mohagames205/HabGrabBot", inline=False)
	embed.add_field(name="Invitelink", value="https://discordapp.com/oauth2/authorize?client_id=349200626955321354&scope=bot&permissions=1024", inline=False)
	embed.set_footer(text="Powered by HabGrab ©")
	await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def help(ctx):
	embed=discord.Embed(title="Er zijn intotaal 3 commands", color=0xffff00)
	embed.add_field(name="$grab (habbonaam)", value="Geeft informatie over de gebruiker", inline=False)
	embed.add_field(name="$help", value="Geeft je alle verschillende commands", inline=False)
	embed.add_field(name="$info", value="Geeft info over de bot", inline=False)
	embed.add_field(name="Vragen over de bot?", value="Contacteer @Mohagames#7389 voor hulp en antwoorden op je vragen.", inline=False)
	embed.add_field(name="Discord server:", value="https://discord.gg/TZjtPk2")
	embed.add_field(name="Github pagina:", value="https://github.com/Mohagames205/HabGrabBot")
	embed.set_footer(text="Powered by HabGrab ©")
	await bot.say(embed=embed)

bot.run(os.getenv('TOKEN'))