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
	habbo = habbo.lower()
	try:
		#haalt de data van de Habbo op
		with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
			data = json.loads(url.read().decode())
			id = data["uniqueId"]
			naamio = data['name']
			motto = data['motto']
			lidsince = data['memberSince']
			
			
		if motto == "":
			motto = ("Geen")
		else:
			motto = motto
		try:
			with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users/{id}/friends") as url:
				data = json.loads(url.read().decode())
				aantal = len(data)
				aantal = str(aantal)
		except:
			aantal = "Onzichtbaar"
			
			
		#embed start hier
		urllib.request.urlretrieve(f"https://www.habbo.nl/habbo-imaging/avatarimage?hb=image&user={habbo}",f"{habbo}.jpg")
		embed=discord.Embed(title="Hier zijn de gegevens van de opgevraagde Habbo: ", color=0xffff00)
		embed.set_thumbnail(url="https://www.justcakenl.tk/host/events.gif")
		embed.set_image(url=f"https://www.justcakenl.tk/host/{habbo}.jpg")
		embed.add_field(name="Naam:" , value=naamio, inline=True)
		embed.add_field(name="Motto:", value=motto, inline=True)
		embed.add_field(name="Lid sinds:" , value=lidsince, inline=True)
		embed.add_field(name="Aantal vrienden:" , value=aantal, inline=True)
		embed.set_footer(text="Powered by HabGrab ©")
		channel = ctx.message.channel
		await bot.say(embed=embed)
		print("Grab gebruikt")

	except:
		embed=discord.Embed(title="Er is iets misgelopen", description=f"De gebruiker bestaat niet of staat onzichtbaar!", color=0xffff00)
		print("Error")
		embed.set_thumbnail(url="https://justcakenl.tk/host/events.gif")
		embed.set_footer(text="Powered by HabGrab ©")
		await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def info(ctx):
	embed=discord.Embed(title="HabGrab info", description="Alle informatie die je zou willen weten over HabGrab", color=0xffff00)
	embed.set_thumbnail(url="https://justcakenl.tk/host/events.gif")
	embed.add_field(name="Creator", value="Deze discord bot is gemaakt door @Mohagames#7389", inline=False)
	embed.add_field(name="Programmeertaal", value="** Python Discord.py 0.16.12**", inline=False)
	embed.add_field(name="Githubpagina", value="https://github.com/Mohagames205/HabGrabBot", inline=False)
	embed.add_field(name="Invitelink", value="https://discordapp.com/oauth2/authorize?client_id=349200626955321354&scope=bot&permissions=1024", inline=False)
	embed.set_footer(text="Powered by HabGrab ©")
	await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def help(ctx):
	embed=discord.Embed(title="Er zijn intotaal 3 commands", color=0xffff00)
	embed.set_thumbnail(url="https://justcakenl.tk/host/events.gif")
	embed.add_field(name="$grab (habbonaam)", value="Geeft informatie over de gebruiker", inline=False)
	embed.add_field(name="$help", value="Geeft je alle verschillende commands", inline=False)
	embed.add_field(name="$info", value="Geeft info over de bot", inline=False)
	embed.set_footer(text="Powered by HabGrab ©")
	await bot.say(embed=embed)
	
@bot.command(pass_context = True)
async def test(ctx, habbo,n):
	n = int(n)
	with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
		data = json.loads(url.read().decode())
		id = data["uniqueId"]

	with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users/{id}/friends") as url:
		data = json.loads(url.read().decode())
		aantal = len(data)
		aantal = str(aantal)
		data = data[n]
		await bot.say(data)
		await bot.say(aantal)
		
@bot.command(pass_context = True)
async def friends(ctx, habbo):
	with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
		data = json.loads(url.read().decode())
		id = data["uniqueId"]
	with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users/{id}/friends") as url:
		data = json.loads(url.read().decode())

	embed=discord.Embed(title=f"Vriendenlijst van {habbo}", color=0xffff00)
	num = 1
	for vriend in data:
		embed.add_field(name=f"{num}", value=f"{vriend['name']}", inline=True)
		num += 1

	embed.set_footer(text="Powered by HabGrab ©")
	await bot.say(embed=embed)
bot.run(os.environ.get("TOKEN"))
