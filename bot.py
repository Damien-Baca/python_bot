# bot.py
from sys import stderr, exit
from os import getenv
from random import choice

from discord import Intents, utils, DMChannel
from discord.ext.commands import Bot
from dotenv import load_dotenv

DEBUG = False
SCREENSHOT_CHANNEL_WARNING = 'Messages in the screenshots channel must contain an attached image. You\'re message has been DELETED!'
CYBERMAN_QUOTES = [
    'DELETE! DELETE! DELETE!',
    'Emotions have tormented you all of your life. Now you will be set free. This is your liberation.',
    'I\'m cold. I\'m so cold...',
    'Destroy them! Destroy them at once!',
    'We have freedom from disease, protection against heat and cold, true mastery.',
    'Every empire has its time, and every empire falls. But that which is dead can live again... In the hands of a believer!'
]

load_dotenv(override=True)
TOKEN = getenv('DISCORD_TOKEN')
GUILD = getenv('DISCORD_GUILD')

bot_intents = Intents.all()
bot = Bot(command_prefix='!', intents=bot_intents)


@bot.event
async def on_ready():
    global guild
    guild = utils.get(bot.guilds, name=GUILD)
    if not guild:
        print(f'Bot is not connected to a Guild. Exiting!', file=stderr)
        exit()

    if bot.user and guild:
        print(f'{bot.user.name} has connected to {guild.name}!')
        members = '\n - '.join([member.name for member in guild.members])
        print(f'Guild Members:\n - {members}')


@bot.event
async def on_message(message):
    if type(message.channel) != DMChannel and message.channel.name == 'screenshots':
        if not message.attachments and guild:
            await message.delete()
            member = utils.get(guild.members, name=message.author.name)
            if member:
                dm = await member.create_dm()
                await dm.send(SCREENSHOT_CHANNEL_WARNING)
    else:
        await bot.process_commands(message)


@bot.command(name='cyberman', help='Prints a Cyber-man quote')
async def quote_cybermen(ctx):
    response = choice(CYBERMAN_QUOTES)
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
else:
    print('Error retrieving DISCORD_TOKEN. Failed to start Bot.', file=stderr)
