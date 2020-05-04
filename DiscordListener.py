import os
import discord
from discord.ext import commands
from rpg_helper.dao.RpgHelperDaoSqlLiteImpl import RpgHelperDaoSqlLiteImpl
from dotenv import load_dotenv
import logging
logging.basicConfig(level=logging.INFO)
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)
logging.info(msg="starting")
bot = commands.Bot(command_prefix='!')

rpgHelper = RpgHelperDaoSqlLiteImpl(database_name='rpg-helper.db')


@bot.command(name='add_inventory')
async def add_inventory(ctx, item):
    logging.info(msg=f"""received message: {ctx.message}\n
        channel name: {ctx.message.channel.name}\n 
        channel id: {ctx.message.channel.id}
        item: {item} \n
        author: {ctx.author}
    """)
    rpgHelper.add_inventory(user=str(ctx.author), user_id=str(ctx.author.id), item=item, channel_id=str(ctx.message.channel.id))
    await ctx.send(f'added inventory {item}')


@bot.command(name='remove_inventory')
async def remove_inventory(ctx, arg):
    logging.info(msg=f'received {ctx.message} {arg}, author {ctx.author}')
    rpgHelper.remove_inventory(arg)

    await ctx.send(f'removing inventory {arg}')

@bot.command(name='view_inventory')
async def view_inventory(ctx):
    logging.info(msg=f'received {ctx.message}, author {ctx.author}')
    items = rpgHelper.get_user_inventory(user_id=str(ctx.author.id), channel_id=str(ctx.message.channel.id))

    def parse_items_func(item):
        return item.item

    parsed_items = list(map(parse_items_func, items))
    await ctx.send(f'Inventory: {parsed_items}')

bot.run(os.getenv('DISCORD_TOKEN'))
