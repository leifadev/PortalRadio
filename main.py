import time
import json
import random
import math
import discord
import os
import sys
import sqlite3
import secret
import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from os import listdir
import datetime
import asyncio
# import the token
from config import *

# shard id
shardids = 1
# shard count
shardcount = 1
# command prefix
commandprefix = ["p!"]

intents = discord.Intents.all()

bot = commands.AutoShardedBot(case_insensitive=True, loop=None, shard_id=shardids, shard_count=shardcount, command_prefix=commands.when_mentioned_or(*commandprefix), help_command=None, intents=intents)

# cogs
try:
	path = f'E:/Coding Shit/Code/PortalRadio/cogs'
	cogs = []
	for f in listdir(path):
		file = f"cogs.{f}".replace('.py', '')
		cogs += [file]
	cogs.remove('cogs.__pycache__')
	#cogs.remove('Cogs.errorhandler')
	print(cogs)
except:
	pass

for extension in cogs:
	bot.load_extension(extension)

# run the bot
print("Running...")
bot.run(config)