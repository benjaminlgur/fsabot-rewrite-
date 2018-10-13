#fsabot using discord.py rewrite by grunt67 made for python 3.7

import discord
from discord.ext import commands
import asyncio
import random

TOKEN = open("fsabottoken.txt", "rt")

bot = commands.Bot(command_prefix='.')


@bot.event
async def on_ready():
    print("NSA Bot is ready.")
    print("Logged in as {0.user}".format(bot))

@bot.command()
async def echo(ctx, *, message):
    await ctx.send(message)

@bot.event
async def on_member_join(member):
    await member.add_roles(discord.utils.get(member.guild.roles, name='Autists'))

@bot.command()
async def add(ctx, *, inrole):
    if inrole[0]=='<' and inrole[1] == '@':
        if len(ctx.message.role_mentions) > 1:
            await ctx.send("Only one role at a time.")
            return
        inrole = ctx.message.role_mentions[0].name
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name = str(inrole))
    try:
        await  user.add_roles(role)
        await ctx.send("The role " + str(role) + " was added to " + str(user))
    except: 
        await ctx.send("Invalid role")

@bot.command()
async def remove(ctx, *, inrole):
    if inrole[0]=='<' and inrole[1] == '@':
        if len(ctx.message.role_mentions) > 1:
            await ctx.send("Only one role at a time")
            return
        inrole = ctx.message.role_mentions[0].name
    user = ctx.message.author
    role = discord.utils.get(user.guild.roles, name = str(inrole))
    try:
        await  user.remove_roles(role)
        await ctx.send("The role " + str(role) + " was removed from " + str(user))
    except: 
        await ctx.send("Invalid role")

@bot.command()
async def heresy(ctx):
    await ctx.send('https://imgur.com/a/kjBxW1o')

@bot.command()
async def purge(ctx, amount=0):
    if ctx.message.author.roles[len(ctx.message.author.roles)-1].permissions.manage_channels == False: #tied permission to purge with mannage channels
        await ctx.send("Don't try that.") 
        return
    try:
        await ctx.channel.purge(limit=amount+2)
        await ctx.send("https://imgur.com/a/6oJct5q")
        await ctx.send(str(amount) + " messeges purged.")
        await asyncio.sleep(4)
        await ctx.channel.purge(limit=2)
    except:
        await ctx.send("You fucked it up.")

#Team code below here

players = []

@bot.command()
async def jointeam(ctx):
    players.append(ctx.message.author.display_name)
    await ctx.send(ctx.message.author.display_name + " added to list.")

@bot.command()
async def showlist(ctx):
    await ctx.send(players)

@bot.command()
async def clearlist(ctx):
    players.clear()

@bot.command()
async def maketeams(ctx):
    teamOne = []
    teamTwo = []
    random.shuffle(players)
    for x in range(0, len(players)):
        if x+1 <= (len(players)/2):
            teamOne.append(players[x])
        else:
            teamTwo.append(players[x])
    await ctx.send("Team 1 is " + ", ".join(teamOne) + " Team 2 is " + ", ".join(teamTwo) +  ".")



bot.run(TOKEN.read())

