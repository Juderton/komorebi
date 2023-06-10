from discord.ext import commands
from discord import app_commands, Interaction
import discord


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.tree.add_command(app_commands.ContextMenu(
            name='Horse React',
            callback=self.horse_react))

    async def horse_react(self,
                          interaction: Interaction,
                          message: discord.Message):
        await interaction.response.defer(ephemeral=True)
        await message.add_reaction('\U0001F434')
        await message.reply(
            'https://tenor.com/view/horse-horse-react-thanos-meme-gif-26303208')


async def setup(bot):
    await bot.add_cog(Fun(bot))
