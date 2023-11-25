import discord
from discord.ext import commands

intents = discord.Intents.all()
intents.members = True
intents.message_content = True
intents.presences = True

# Begin Config

prefix = '!'
CHANNEL_ID = 1166823413336252546

# End Config


bot = commands.Bot(command_prefix=prefix, intents=intents)



