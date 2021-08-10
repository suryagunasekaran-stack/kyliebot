#bot.py
import os
import discord
import random
#from dotenv import load_dotenv

#load_dotenv()
TOKEN = 'ODUxMzI0NTUyOTU1ODIyMDgx.YL2nxg.XDvGAtkbs3vDWlFZzckf-93cba4'
GUILD = 'League Of Feeders'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    kylie_quotes = [
        'Thats fucked up',
        'shut up retard',
        'OMG shut up',
        'doomas',
        '*disjoins discord*',

    ]

    if message.content == 'kylie!':
        response = random.choice(kylie_quotes)
        await message.channel.send(response)

client.run(TOKEN)
