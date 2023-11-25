import discord
import pymongo
from discord.ui import Button, View
from discord.ext import commands
from pymongo import MongoClient
from bson import ObjectId
from app.services.database import db_client



class MainView(discord.ui.View):

    def __init__(self, item_var, key_var, db):
        self.item_var = item_var
        self.key_var = key_var
        self.db = db
        super().__init__(timeout=None)
        self.add_buttons()

    def add_buttons(self):
        button_one = discord.ui.Button(label=self.item_var, style=discord.ButtonStyle.blurple)

        async def button_example(interaction: discord.Interaction):
            await interaction.response.edit_message(content="", view=ConfirmView(self.item_var, self.key_var, self.db))  

        button_one.callback = button_example
        self.add_item(button_one)        


# Confirmation buttons to ask for deletion or return
class ConfirmView(discord.ui.View):

    def __init__(self, item_var, key_var, db):
        self.item_var = item_var
        self.key_var = key_var
        self.db = db
        super().__init__(timeout=None)    

    @discord.ui.button(label = "Remove", style = discord.ButtonStyle.red)
    async def button_callback1(self, interaction: discord.Interaction, button):
        self.db.groceries_log.delete_one( { "_id" : ObjectId(self.key_var) } )
        await interaction.response.edit_message(content="Deleting...", view=None, delete_after=1.0)

    @discord.ui.button(label = "Return", style = discord.ButtonStyle.green)
    async def button_callback2(self, interaction: discord.Interaction, button):
        await interaction.response.edit_message(content="", view=MainView(self.item_var, self.key_var, self.db)) 


async def handle(ctx):
    channel1 = str(ctx.channel.id)

    db = getattr(db_client, channel1)

    groceries = db.groceries_log.find({},{"item":1})
    
    current_keypair = {}
    for i in groceries:
        current_keypair[i["_id"]] = i["item"]


    if not current_keypair:
        await ctx.send(f"There are currently no items in this channel's shopping list.")
    else:
        for key in current_keypair:
            await ctx.send("", view=MainView(current_keypair[key], key, db))
