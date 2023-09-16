import os
import discord
from pymongo import MongoClient

# Get the Discord token from the environment variable
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

# Define MongoDB connection details using environment variables
MONGO_HOST = os.getenv('MONGOHOST')
MONGO_PORT = os.getenv('MONGOPORT')
MONGO_USER = os.getenv('MONGOUSER')
MONGO_PASSWORD = os.getenv('MONGOPASSWORD')
MONGO_URL = os.getenv('MONGO_URL')

# Initialize the MongoDB client
client = MongoClient(host=MONGO_HOST, port=int(MONGO_PORT), username=MONGO_USER, password=MONGO_PASSWORD, authSource='admin')

# Access your MongoDB database
db = client['clicker']

# Access a specific collection in the database
collection = db['fbe']

# Create a Discord bot
bot = discord.Bot()

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Your other bot commands and event handlers can go here

# Run the bot with the Discord token
bot.run(DISCORD_TOKEN)
