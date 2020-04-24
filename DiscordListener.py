import os
import discord
from discord.ext import commands
from dao.RpgHelperDaoSqlLiteImpl import RpgHelperDaoSqlLiteImpl

print('Starting')
bot = commands.Bot(command_prefix='!')

rpgHelper = RpgHelperDaoSqlLiteImpl(database_name='rpg-helper.db')


@bot.command(name='add_inventory')
async def add_inventory(ctx, item):
    print(f"""received message: {ctx.message}\n
        channel name: {ctx.message.channel.name}\n 
        item: {item} \n
        author: {ctx.author}
    """)
    rpgHelper.add_inventory(str(ctx.author), ctx.message.channel.name, item)
    await ctx.send(f'added inventory {item}')


@bot.command(name='remove_inventory')
async def remove_inventory(ctx, arg):
    print(f'received {ctx.message} {arg}, author {ctx.author}')
    rpgHelper.remove_inventory(arg)

    await ctx.send(f'removing inventory {arg}')


bot.run(DISCORD_TOKEN)
