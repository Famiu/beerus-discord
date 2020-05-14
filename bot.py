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

client.run(os.environ.get('BOT_TOKEN'))
print("Bot initialized with token: {0}".format(os.environ.get('BOT_TOKEN')))
