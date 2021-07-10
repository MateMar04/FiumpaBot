import discord
import os
import requests

client = discord.Client()


@client.event
async def on_ready():
    print("{0.user}".format(client))

@client.event
async def on_message(message):
    if message.author != client.user:
        if message.content.startswith("&help"):
           await message.channel.send("GUIA DE AYUDA")
        return


client.run("ODYzNTQyNDcxODA0MTkwNzUx.YOoamQ.wvtcb_JhmKoY_CYCdFWUkZQYmF0")
