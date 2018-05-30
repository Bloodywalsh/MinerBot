import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random

Client = discord.Client()
client = commands.Bot(command_prefix = "!")


@client.event
async def on_ready():
    print("active")

@client.event
async def on_message(message):
    if message.content.upper().startswith('!VER'):
        await client.send_message(message.channel, "**Ver 1.0.1**")
