import os
import discord

client = discord.Client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$ping'):
        await message.channel.send("Pong!")

token : str = os.environ['BOT_TOKEN']

print(f"Token: {token}")
client.run(os.environ['BOT_TOKEN'])
