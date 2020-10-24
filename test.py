import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('へい'):
        await message.channel.send('ﾎｼﾏﾁｰ!!')

client.run('NzY5NTIwNzAyNDI4MTUxODM4.X5QOAA.gLHgNfYoNzqhAy6Iz2ZOE5TaAWc')