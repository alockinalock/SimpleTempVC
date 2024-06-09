import discord
from discord.ext import commands
from discord import app_commands

class VoiceChannelDelete(commands.Cog):
                

        def __init__(self, bot):
                self.bot = bot


        @commands.Cog.listener()
        async def on_ready(self):
                print(f'{self.__class__.__name__} cog loaded.')


        async def delete_voice(self, interaction: discord.Interaction, category: discord.CategoryChannel, sel_channel: discord.VoiceChannel):
                if sel_channel in category.channels:
                        await sel_channel.delete()
                else:
                        print("WARNING: Channel deletion failed!!")


async def setup(bot):
        await bot.add_cog(VoiceChannelDelete(bot))