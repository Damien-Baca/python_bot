# bot_example.py
from os import getenv
from random import choice

from discord import Intents
from discord.ext.commands import Bot
from dotenv import load_dotenv


load_dotenv(override=True)
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')

bot_intents = Intents.all()
bot = Bot(command_prefix='!', intents=bot_intents)


@bot.event
async def on_ready():
    if bot.user:
        print(f'{bot.user.name} has connected to {GUILD}!')


@bot.command(name='cyberman', help='Prints a Cyber-man quote')
async def quote_cybermen(ctx):
    cyberman_quotes = [
        'DELETE! DELETE! DELETE!',
        'Emotions have tormented you all of your life. Now you will be set free. This is your liberation.',
        'I\'m cold. I\'m so cold...',
        'Destroy them! Destroy them at once!',
        'We have freedom from disease, protection against heat and cold, true mastery.',
        'Every empire has its time, and every empire falls. But that which is dead can live again... In the hands of a believer!'
    ]
    response = choice(cyberman_quotes)
    await ctx.send(response)


@bot.command(name='roll_dice', help='Simulates rolling dice')
async def roll_dice(cxt, number_of_dice: int, number_of_sides: int):
    rolls = [
        str(choice(range(1, number_of_sides+1)))
        for _ in range(number_of_dice)
    ]
    roll_str = ', '.join(rolls)
    response = f'Dice Rolls: {roll_str}'
    await cxt.send(response)

if TOKEN:
    bot.run(TOKEN)
