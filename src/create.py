import discord
from discord.ext import commands
from discord import app_commands

class CreateVoiceChannel(commands.Cog):


        def __init__(self, bot):
                self.bot = bot


        @commands.Cog.listener()
        async def on_ready(self):
                print(f'{self.__class__.__name__} cog loaded.')
        

        async def create_voice(self, interaction: discord.Interaction, category: discord.CategoryChannel, name: str, member_count: int) -> discord.VoiceChannel:
                channel_created = await category.create_voice_channel(name, user_limit=member_count)
                
                if channel_created is not None:
                        await interaction.response.send_message(f"Temporary voice channel created under the name: {name}")
                        return channel_created
                else:
                        await interaction.response.send_message("Failed to create temporary voice channel")


async def setup(bot):
        await bot.add_cog(CreateVoiceChannel(bot))
