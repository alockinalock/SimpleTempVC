import discord
from discord.ext import commands
from discord import app_commands

class VoiceChannelCheck(commands.Cog):
                
        def __init__(self, bot):
                self.bot = bot

async def setup(bot):
        await bot.add_cog(VoiceChannelCheck(bot))