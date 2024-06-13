import discord
from discord.ext import commands
from discord import app_commands

class ManageVoiceChannels(commands.Cog):
                
        def __init__(self, bot):
                self.bot = bot

        async def manage_temp_voice_channels(self, category: discord.CategoryChannel, channels):
            for current_channel in category.channels:
                   if isinstance(current_channel, discord.VoiceChannel) and current_channel in channels:
                        if len(current_channel.members) == 0:
                                try:
                                        await current_channel.delete()
                                        print(f"{current_channel.name} deleted.")
                                except Exception as e:
                                        print(f"WARNING. CHANNEL DELETION FAILED. EXCEPTION RAISED: {e}")
                               
                                                       

async def setup(bot):
        await bot.add_cog(ManageVoiceChannels(bot))
