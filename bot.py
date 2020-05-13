import os
import discord

client = discord.client()

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$ping'):
        await message.channel.send("Pong!")

client.run(os.environ['BOT_TOKEN'])
