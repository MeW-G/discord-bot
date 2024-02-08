import discord
import os
from discord.ext import commands
import dotenv
from dotenv import load_dotenv
load_dotenv()

token = os.getenv("TOKEN")
# Erstellen des Bot-Clients
bot = commands.Bot(command_prefix='-', intents = None)

# Event-Handler für das Event 'on_ready' (wird aufgerufen, wenn der Bot erfolgreich gestartet ist)
@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user.name} ({bot.user.id})')
    print('------')

# Event-Handler für das Event 'on_message' (wird aufgerufen, wenn eine Nachricht im Server empfangen wird)
@bot.event
async def on_message(message):
    # Verhindern, dass der Bot seine eigenen Nachrichten liest (um Endlosschleifen zu vermeiden)
    if message.author == bot.user:
        return
    # Nachrichten im gewünschten Kanal lesen


    # Wichtig: Die Zeile unten nicht vergessen, um die anderen Event-Handler (wie on_message) weiterhin zu aktivieren
    await bot.process_commands(message)

# Bot mit dem Discord-Server verbinden (token aus .env)
bot.run(token)
