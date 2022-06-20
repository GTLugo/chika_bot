import os
import asyncio
#import random
from datetime import datetime

import discord
from discord import app_commands

TOKEN = os.environ['DISCORD_TOKEN']
GUILD = int(os.environ['GUILD_ID'])
GTLUGO = int(os.environ['GTLUGO_ID'])
ANNOUNCE = int(os.environ['ANNOUNCE_ID'])
FOLLOW = int(os.environ['FOLLOW_ID'])

hololive = ['hololive', 'holo']
nijisanji = ['nijisanji', 'niji']

class bot_client(discord.Client):
  def __init__(self):
    super().__init__(intents=discord.Intents.all())
    self.synced = False

  async def on_ready(self):
    await self.wait_until_ready()
    if not self.synced:
      await tree.sync(guild = discord.Object(id = GUILD))
      self.synced = True
      print(f'Synced commands!')
    print(f'Hi, friends! It\'s {self.user}.')
    
client = bot_client()
tree = app_commands.CommandTree(client)

@tree.command(name = 'livenow', description = 'Curated list of vtubers live now', guild = discord.Object(id = GUILD))
async def self(interaction: discord.Interaction, group: str):
  if group in hololive:
    await interaction.response.send_message(f'Showing live hololive vtubers!')
  elif group in nijisanji:
    await interaction.response.send_message(f'Showing live nijisanji livers!')
  else:
    await interaction.response.send_message(f'Unknown group: {group}')
  
@tree.command(name = 'livetoday', description = 'Curated list of vtubers live today', guild = discord.Object(id = GUILD))
async def self(interaction: discord.Interaction, group: str):
  if group in hololive:
    await interaction.response.send_message(f'Showing live and upcoming hololive vtubers!')
  elif group in nijisanji:
    await interaction.response.send_message(f'Showing live and upcoming nijisanji livers!')
  else:
    await interaction.response.send_message(f'Unknown group: {group}')

client.run(TOKEN)