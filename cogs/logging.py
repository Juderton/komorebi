from discord.ext import commands
import discord


class Logging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_message_delete(self,
                                    payload: discord.RawMessageDeleteEvent):
        message = payload.cached_message

        if not message.author.bot:
            channel = message.guild.get_channel(1115073596310683679)
            embed = discord.Embed()
            embed.color = 0xED4245
            embed.description = f'**Message sent by {message.author.mention} deleted in {message.channel.mention}**'
            embed.timestamp = discord.utils.snowflake_time(message.id)

            embed.add_field(name='', value=message.clean_content)
            embed.set_author(name=message.author._user,
                             icon_url=message.author.avatar.url)
            await channel.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Logging(bot))
