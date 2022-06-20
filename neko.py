from datetime import datetime
import os
import random

from dotenv import load_dotenv
import asyncio

import discord
from discord.ext import commands
from discord_slash import SlashCommand, SlashContext

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = [int(os.getenv('GUILD_ID'))]
GTLUGO = int(os.getenv('GTLUGO_ID'))
ANNOUNCE = int(os.getenv('ANNOUNCE_ID'))
FOLLOW = int(os.getenv('FOLLOW_ID'))

bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())
slash = SlashCommand(bot, sync_commands=True)

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


def rand(percent=50) -> bool:
    return random.randrange(100) < percent


@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.channel.id == FOLLOW:
        channel_to_send_to = bot.get_channel(ANNOUNCE)
        await channel_to_send_to.send(message.clean_content, embed=message.embeds[0])
        print(f'Posted message from {message.guild.name}')


@slash.slash(name="headpat", description="Give Chika a nice headpat.", guild_ids=GUILD)
async def _headpat(ctx: SlashContext):
    print(f'{ctx.author} used headpat at {datetime.now()}!')
    message = ""
    if ctx.author_id == GTLUGO:
        message = "I love you, Gabe~ <3"
    else:
        message = "Thank you~"
    await ctx.send(message)


@slash.slash(name="cuddle", description="Ask Chika for cuddles.", guild_ids=GUILD)
async def _cuddle(ctx: SlashContext):
    print(f'{ctx.author} used cuddle at {datetime.now()}!')
    message = ""
    if ctx.author_id == GTLUGO:
        message = "Mmmm, nice~ <3"
    else:
        if rand(10):
            message = "Comfy~ :)"
        else:
            message = "No thanks! :)"
    await ctx.send(message)


@slash.slash(name="waifu", description="Ask Chika to be your waifu.", guild_ids=GUILD)
async def _waifu(ctx: SlashContext):
    print(f'{ctx.author} used waifu at {datetime.now()}!')
    message = ""
    if ctx.author_id == GTLUGO:
        message = "Of course I'm your waifu! <3"
    else:
        message = "I'm not your waifu; we're friends! :)"
    await ctx.send(message)

bot.run(TOKEN)
