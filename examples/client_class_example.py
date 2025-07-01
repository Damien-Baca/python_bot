# client.py
import sys
import os
import random

import discord
from dotenv import load_dotenv

load_dotenv(override=True)
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')


class DiscordClient(discord.Client):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD)
        print(f'{self.user} has connected to {guild.name}!')

        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}\n')

    async def on_member_join(member):
        await member.create_dm()
        await member.dm_channel.send(f'Hi {member.name}, welcome to the server! Follow the rules or be DELETED!')

    async def on_message(self, message):
        cyberman_quotes = [
            'DELETE! DELETE! DELETE!',
            'Emotions have tormented you all of your life. Now you will be set free. This is your liberation.',
            'I\'m cold. I\'m so cold...',
            'Destroy them! Destroy them at once!',
            'We have freedom from disease, protection against heat and cold, true mastery.',
            'Every empire has its time, and every empire falls. But that which is dead can live again... In the hands of a believer!'
        ]
        if message.author == self.user:
            return

        if message.content == 'cyberman!':
            response = random.choice(cyberman_quotes)
            await message.channel.send(response)
        elif message.content == 'raise-exception!':
            raise discord.DiscordException

    async def on_error(self, event, *args, **kwargs):
        with open('err.log', 'a') as f:
            if event == 'on_message':
                f.write(f'Unhandled message {args[0]}\n')
            else:
                raise


client_intents = discord.Intents.all()
client = DiscordClient(intents=client_intents)
client.run(TOKEN)
