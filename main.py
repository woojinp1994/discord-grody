import os
from dotenv import load_dotenv
load_dotenv(override=True)

from app.services.discord_client import bot, CHANNEL_ID

BOT_TOKEN = os.getenv('BOT_TOKEN')


# Import controllers from dir

for filename in os.listdir('./app/controllers'):
    if filename.endswith('.py'):
        filename = filename.rstrip('.py')
        eval(f"exec('from app.controllers import {filename}')")


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Grody is ready and online! Use the !info command to learn more about Grody as well as a list of commands.")


@bot.command(name='info')
async def on_info(ctx):
    await on_info_controller.handle(ctx)

@bot.command(name='add')
async def on_add(ctx, *args):
    await on_add_controller.handle(ctx, *args)

@bot.command(name='clear')
async def on_clear(ctx):
    await on_clear_controller.handle(ctx)    

@bot.command(name='list')
async def on_list(ctx):
    await on_list_controller.handle(ctx)       


bot.run(BOT_TOKEN)



