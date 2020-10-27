import discord
import os
import traceback
from datetime import datetime, timedelta

#token
token = os.environ['DISCORD_BOT_TOKEN']


client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content('ﾎｼﾏﾁｰ!!') :
        await message.channel.send('ﾎｼﾏﾁｰ!!')

#VC入退室
@client.event
async def on_voice_state_update(member,before,after) :
    if member.guild.id == 769396177221058600 and (before.channel != after.channel):
        now = datetime.utcnow() + timedelta(hours=9)
        alert_channel = client.get_channel(769718981908758589)
        if before.channel is None: 
            msg = f'{now:%m/%d-%H:%M:%S} に {member.name} さんが VC"{after.channel.name}" に参加しました。'
            await alert_channel.send(msg)
        elif after.channel is None: 
            msg = f'{now:%m/%d-%H:%M:%S} に {member.name} さんが VC"{before.channel.name}" から退出しました。'
            await alert_channel.send(msg)
        else:
            msg = f'{now:%m/%d-%H:%M:%S} に {member.name} さんが VC"{before.channel.name}" から VC"{after.channel.name}" に移動しました。'
            await alert_channel.send(msg)

client.run(token)