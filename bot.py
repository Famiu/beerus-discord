import os
import discord
import logging

# Basic log configuration
logger = logging.getLogger('discord')

client = discord.Client()

authorized_users = [244275194070433795]
guildprefix = {}

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.content.startswith(guildprefix.get(message.guild.id, "~")):
        await respond_to_command(message)

async def respond_to_command(message):
    message_words = message.content.split()
    command = message_words[0][1:]
    arguments = " ".join(message_words[1:])

    if(command == "ping"):
        await message.channel.send("Ponga!")

    elif(command == "eval"):
        print(message.author.id)
       
        if message.author.id in authorized_users:
            await message.channel.send(eval(arguments))

client.run(os.environ.get('BOT_TOKEN'))
