from discord.ext import commands
from discord import app_commands, Interaction
from typing import Literal


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description='Reloads an extension')
    async def reload(self,
                     interaction: Interaction,
                     extension: Literal['admin', 'images'],
                     sync_commands: bool):

        if interaction.user.id == 688832593570955354:
            content = f'Reloading `{extension}` extension...'
            await interaction.response.send_message(content=content)
            await self.bot.reload_extension(f'cogs.{extension}')
            content = f'{content}\nDone'
            await interaction.edit_original_response(content=content)

            if sync_commands:
                content = f'{content}\nSyncing commands...'
                await interaction.edit_original_response(
                    content=content)
                await self.bot.tree.sync()
                content = f'{content}\nDone'
                await interaction.edit_original_response(
                    content=content)
        else:
            await interaction.response.send_message(
                content='You do not have permission to execute this command',
                ephemeral=True)


async def setup(bot):
    await bot.add_cog(Admin(bot))
