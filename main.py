import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix="&", intents=intents)


@client.event
async def on_ready():
    activity = discord.Game(name="&ayuda")
    await client.change_presence(activity=activity)
    print("{0.user}".format(client) + " online")


@client.command()
async def ayuda(ctx):
    await ctx.send("GUIA DE AYUDA\n"
                   "------------------\n"
                   "&join ---> \n"
                   "&leave --> \n"
                   "&pause --> \n"
                   "&resume --> \n"
                   "&stop --> \n")


@client.command(pass_context=True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Chakal, tenes que estar en un canal de voz para que pueda entrar viiiiiiiiiiste")


@client.command(pass_context=True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Me tome el palo chakal")
    else:
        await ctx.send("Que flashas, no estoy en un canal de voz")


@client.command(pass_context=True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Pelotudo no estoy diciendo nada")


@client.command(pass_context=True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("Pelotudo no estoy pausado")


@client.command(pass_context=True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


client.run("TOKEN")
