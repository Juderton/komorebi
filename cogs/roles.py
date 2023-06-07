from discord.ext import commands
from discord import app_commands, Interaction
import discord

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description='Changes your role color')
    @app_commands.describe(color='The hex color code of your role color (e.g. #ffffff)')
    async def color(self, interaction: Interaction, color: str):
        has_role = False

        for role in interaction.user.roles:
            if role.name.startswith('#'):
                has_role = True
                color_role = role
                break

        try:
            if has_role:
                await color_role.edit(name=color, color=int(color[1:], 16))
            else:
                color_role = await interaction.guild.create_role(name=color, color=int(color[1:], 16))
                await interaction.user.add_roles(color_role)
        except ValueError:
            await interaction.response.send_message(
                content='Invalid hex color code',
                ephemeral=True)

        await interaction.response.send_message(
            content=f'Updated your color role to {color_role.mention}',
            ephemeral=True)


async def setup(bot):
    await bot.add_cog(Roles(bot))