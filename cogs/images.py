from discord.ext import commands
from discord import app_commands, Interaction
import requests


class Images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(description='Generates a random image of a cat')
    async def cat(self, interaction: Interaction):
        api_key = open('tokens/cat_api_key.txt').readline()
        url = f'https://api.thecatapi.com/v1/images/search?api_key={api_key}'
        response = requests.get(url=url)
        image = response.json()[0]['url']

        await interaction.response.send_message(content=image)

    @app_commands.command(description='Generates a random image of a dog')
    async def dog(self, interaction: Interaction):
        api_key = open('tokens/dog_api_key.txt').readline()
        url = f'https://api.thedogapi.com/v1/images/search?api_key={api_key}'
        response = requests.get(url=url)
        image = response.json()[0]['url']

        await interaction.response.send_message(content=image)


async def setup(bot):
    await bot.add_cog(Images(bot))
