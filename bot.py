import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True
bot = commands.Bot(command_prefix='/', intents=intents)
token = open('tokens/bot_token.txt').readline()


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(
        status=discord.Status.do_not_disturb,
        activity=discord.Activity(type=discord.ActivityType.listening,
                                  name='commands'))
    print('Changed presence')

    for file in os.scandir('cogs'):
        if file.name.endswith('.py'):
            await bot.load_extension(f'cogs.{file.name[:-3]}')

    print('Loaded extensions from cogs')
    print('Syncing commands...')
    await bot.tree.sync()
    print('Synced commands')
    print(f'{bot.user} is ready!')

bot.run(token)
