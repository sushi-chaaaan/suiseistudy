import discord
import os
import traceback


token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('ﾎｼﾏﾁｰ!!') :
        await message.channel.send('ﾎｼﾏﾁｰ!!')

client.run(token)

#test