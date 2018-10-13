#fsabot using discord.py rewrite by grunt67 made for python 3.7

import discord
from discord.ext import commands

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

bot.run(TOKEN.read())

