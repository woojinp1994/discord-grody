import discord

from app.services.database import db_client

async def handle(ctx, *args):
    author = ctx.author
    channel1 = 'g' + str(ctx.channel.id)

    db = getattr(db_client, 'grocerieslog')
    
    # switch tuple from arguments into string list to be ingested by MongoDB
    item = ' '.join(map(str, args[:]))
    item = item.split(',')
    
    add_list = []

    # iterate over the list of items
    for i in item:
        # create a new MongoDB document dict
        doc = {}

        doc['item'] = i
        doc['author'] = author.id

        # add the MongoDB document to the list
        add_list += [doc]

    db[channel1].insert_many(add_list)
    
    await ctx.send(f"{item} has been added to this channel's grocery list by {author.mention}.")
