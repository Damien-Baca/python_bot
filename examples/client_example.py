# client.py
import sys
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


client_intents = discord.Intents.all()
client = discord.Client(intents=client_intents)


@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(f'{client.user} has connected to {guild.name}!')

    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}\n')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to the server! Follow the rules or be DELETED!')


@client.event
async def on_message(message):
    cyberman_quotes = [
        'DELETE! DELETE! DELETE!',
        'Emotions have tormented you all of your life. Now you will be set free. This is your liberation.',
        'I\'m cold. I\'m so cold...',
        'Destroy them! Destroy them at once!',
        'We have freedom from disease, protection against heat and cold, true mastery.',
        'Every empire has its time, and every empire falls. But that which is dead can live again... In the hands of a believer!'
    ]
    if message.author == client.user:
        return

    if message.content == 'cyberman!':
        response = random.choice(cyberman_quotes)
        await message.channel.send(response)
    elif message.content == 'raise-exception!':
        raise discord.DiscordException


@client.event
async def on_error(event, *args, **kwargs):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message {args[0]}\n')
        else:
            raise

client.run(TOKEN)
