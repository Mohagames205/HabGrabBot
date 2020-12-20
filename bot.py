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
from dotenv import load_dotenv

cp = '$'
bot = commands.Bot(command_prefix=cp)
bot.remove_command("help")
logourl = "https://file.mohamedelyousfi.be/taRO5/PADAmOpa34.gif/raw"
print('Bot is aan het laden...')
load_dotenv()

@bot.event
async def on_ready():
    await bot.user.edit(username="HabGrab")
    await bot.change_presence(activity=discord.Game(name='Use {}help | HabGrab ©'.format(cp)))
    print('Bot is geladen als')
    print(bot.user.name)
    print(bot.user.id)


@bot.command()
async def grab(ctx, habbo):
    habbo = habbo.lower()
    try:
        # haalt de data van de Habbo op
        with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
            data = json.loads(url.read().decode())
            id = data["uniqueId"]
            naamio = data['name']
            motto = data['motto']
            lidsince = data['memberSince']

        if motto == "":
            motto = "Geen"
        else:
            motto = motto
        try:
            with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users/{id}/friends") as url:
                data = json.loads(url.read().decode())
                aantal = str(len(data))
        except:
            aantal = "Onzichtbaar"

        # embed start hier
        embed = discord.Embed(title="Requested Habbo:", color=0xffff00)
        embed.set_thumbnail(url=logourl)
        embed.set_image(url=f"https://www.habbo.nl/habbo-imaging/avatarimage?hb=image&user={habbo}")
        embed.add_field(name="Name", value=naamio, inline=True)
        embed.add_field(name="Motto", value=motto, inline=True)
        embed.add_field(name="Player since", value=lidsince, inline=False)
        embed.add_field(name="Number of friends", value=aantal, inline=False)
        embed.set_footer(text="Powered by HabGrab ©")
        await ctx.send(embed=embed)

    except BaseException as e:
        embed = discord.Embed(title="Something went wrong!",
                              description=f"The requested player does not exist or is invisible.", color=0xffff00)
        print(e)
        embed.set_thumbnail(url=logourl)
        embed.set_footer(text="Powered by HabGrab ©")
        await ctx.send(embed=embed)


@bot.command()
async def info(ctx):
    embed = discord.Embed(title="Info",
                          color=0xffff00)
    embed.set_thumbnail(url=logourl)
    embed.add_field(name="Creator", value="This discord bot was made by Mohamed#0002", inline=False)
    embed.add_field(name="Language", value="Python", inline=False)
    embed.add_field(name="Github", value="https://github.com/Mohagames205/HabGrabBot", inline=False)
    embed.add_field(name="Invite",
                    value="[Invite](https://discord.com/oauth2/authorize?client_id=643538663145340928&scope=bot&permissions=0)",
                    inline=False)
    embed.set_footer(text="Powered by HabGrab ©")
    await ctx.send(embed=embed)


@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Commandlist", color=0xffff00)
    embed.set_thumbnail(url=logourl)
    embed.add_field(name="`$grab <username>`", value="Gives information about the player", inline=False)
    embed.add_field(name="`$help`", value="Shows this menu", inline=False)
    embed.add_field(name="`$info`", value="Shows info about the discord bot", inline=False)
    embed.set_footer(text="Powered by HabGrab ©")
    await ctx.send(embed=embed)


@bot.command()
async def friends(ctx, habbo):
    with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users?name={habbo}") as url:
        data = json.loads(url.read().decode())
        id = data["uniqueId"]
    with urllib.request.urlopen(f"https://www.habbo.nl/api/public/users/{id}/friends") as url:
        data = json.loads(url.read().decode())

    embed = discord.Embed(title=f"Vriendenlijst van {habbo}", color=0xffff00)
    num = 1
    for vriend in data:
        embed.add_field(name=f"{num}", value=f"{vriend['name']}", inline=True)
        num += 1

    embed.set_footer(text="Powered by HabGrab ©")
    await ctx.send(embed=embed)


bot.run(os.environ.get("TOKEN"))
