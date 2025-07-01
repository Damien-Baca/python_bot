# bot.py
from os import getenv

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')


class DiscordBot(commands.Bot):
    async def on_ready(self):
        guild = discord.utils.get(self.guilds, name=GUILD)
        print(f'{self.user.name} has connected to {guild.name}!')


bot_intents = discord.Intents.all()
bot = DiscordBot(command_prefix='!', intents=bot_intents)

bot.run(TOKEN)
