import os
import discord
import logging

# Basic log configuration
logger = logging.getLogger('discord')

client = discord.Client()

guildprefix = {}

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith(guildprefix.get(message.guild.id, "~")):
        respond_to_command(message)

async def respond_to_command(message):
    message_words = message.split()
    command = message_words[0][1:]
    arguments = " ".join(message_words[1:])

    if(command == "ping"):
        await message.channel.send("Pong!")

    elif(command == "eval"):
        await message.channel.send(eval(arguments))

client.run(os.environ.get('BOT_TOKEN'))
