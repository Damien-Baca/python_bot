# bot.py
from os import getenv

# import sys

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')

bot_intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=bot_intents)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to {GUILD}!')

bot.run(TOKEN)
