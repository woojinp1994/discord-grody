import discord

from app.services.database import db_client

async def handle(ctx):
    author = ctx.author
    channel1 = str(ctx.channel.id)

    db = getattr(db_client, channel1)

    db.groceries_log.drop()

    await ctx.send(f"All items in this channel's grocery list has been cleared by {author.mention}.")
    