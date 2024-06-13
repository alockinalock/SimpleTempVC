import discord
import os
import asyncio

from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands, tasks

# --------------------------------------------------------------------------------------------------------

load_dotenv()
token = os.getenv("token")
# legacy commands config
bot = commands.Bot(command_prefix='^', intents = discord.Intents.all())
bot.working_category = None
bot.managed_channels = []

# --------------------------------------------------------------------------------------------------------

@bot.event
async def on_ready():
        print(f"Attempting to load {len(await bot.tree.sync())} command(s).")
        try:
                print(f"\nCommands successfully loaded. Bot is operational.")
        except Exception as error_msg:
                print(error_msg)

        # load all cogs in the src directory
        current_working_directory = os.path.dirname(os.path.abspath(__file__))
        extension_directory = "src"
        target_directory = os.path.join(current_working_directory, extension_directory)
        extension_files = [file for file in os.listdir(target_directory) if file.endswith(".py")]

        for file in extension_files:
                file_name = file[:-3]
                full_extension_file_path = f"{extension_directory}.{file_name}"
                await bot.load_extension(full_extension_file_path)


# --------------------------------------------------------------------------------------------------------

@bot.tree.command(name="config", description="Select the category which temporary voice channels will be created under.")
async def command_configure(interaction: discord.Interaction, category: discord.CategoryChannel):
        await interaction.response.send_message(f"Temporary voice channels will be created under the category: {category}")
        bot.working_category = category
        management.start()


@bot.tree.command(name="create-voice-channel", description="Create a temporary voice channel.")
@app_commands.describe(name="Name of the voice channel", count="Voice channel member limit")
async def command_create(interaction: discord.Interaction, name: str = "Temp", count: int = None):
        cog = bot.get_cog('CreateVoiceChannel')
        if cog is not None:
                chnl = await cog.create_voice(interaction, bot.working_category, name, count)
                bot.managed_channels.append(chnl)

@bot.tree.command(name="del")
async def test_delete(interaction: discord.Interaction, channel: discord.VoiceChannel):
        cog = bot.get_cog("VoiceChannelDelete")
        if cog is not None:
                await cog.delete_voice(interaction, bot.working_category, channel)


@tasks.loop(seconds=300)
async def management():
        cog = bot.get_cog("ManageVoiceChannels")
        if cog is not None:
                await cog.manage_temp_voice_channels(bot.working_category, bot.managed_channels)

# --------------------------------------------------------------------------------------------------------

if __name__ == "__main__":
        #print(f"Booting {bot.user} with both legacy and slash commands.")
        bot.run(token)
