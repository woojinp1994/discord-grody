import discord


async def handle(ctx):
    embed = discord.Embed(
        title='Information About Grody',
        description='Grody-Bot keeps track of your grocery list, and allows you to easily add and remove items. Collaborate with others to manage your shopping list. All shopping lists are channel-specific (TBA).'
    )
    await ctx.send(embed=embed)
