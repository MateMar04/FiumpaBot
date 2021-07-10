import discord
import os
import requests

client = discord.Client()


@client.event
async def on_ready():
    activity = discord.Game(name="&ayuda")
    await client.change_presence(status=discord.Status.idle, activity=activity)
    print("{0.user}".format(client) + " online")


@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("&ayuda"):
            await message.channel.send("GUIA DE AYUDA")
        return


client.run("ODYzNTQyNDcxODA0MTkwNzUx.YOoamQ.wvtcb_JhmKoY_CYCdFWUkZQYmF0")
