import discord
import os
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TOKEN")
# Erstellen des Bot-Clients
bot_intents = discord.Intents.default()
bot = commands.Bot(command_prefix ='-', intents = bot_intents)

client = bot
CHANNEL_ID = 1121965331737481258  # Replace with the actual channel ID
# Event-Handler für das Event 'on_ready' (wird aufgerufen, wenn der Bot erfolgreich gestartet ist)
@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user.name} ({bot.user.id})')
    print('------')

# Specify the channel ID where you want the bot to send the message


# Event to run when the bot is ready
    # Fetch the channel object
    channel = client.get_channel(CHANNEL_ID)

    if channel:
        # Send a message to the specified channel
        await channel.send("I'm online now!")

# Event-Handler für das Event 'on_message' (wird aufgerufen, wenn eine Nachricht im Server empfangen wird)
@bot.event
async def on_message(message):
    print("a message has been sent")
    if message.author == bot.user: #simple guard against bots
        return
    # Wichtig: Die Zeile unten nicht vergessen, um die anderen Event-Handler (wie on_message) weiterhin zu aktivieren
    if message.content:
        await message.channel.send(message.content)

    await bot.process_commands(message)

# Bot mit dem Discord-Server verbinden (token aus .env)
bot.run(token)
