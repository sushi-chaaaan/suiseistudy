import discord
import os
import traceback
from datetime import datetime, timedelta
import sys
import requests
from discord import message

### イベントハンドラ一覧 #################################################
# async def の後を変えるだけで実行されるイベンドが変わる
# メッセージ受信時に実行：   on_message(message)
# Bot起動時に実行：      on_ready(message)
# リアクション追加時に実行:  on_reaction_add(reaction, user)
# 新規メンバー参加時に実行： on_member_join(member)
# ボイスチャンネル出入に実行： on_voice_state_update(member, before, after)
###################################################################

token = os.environ['DISCORD_BOT_TOKEN']
yahoo_apiid = os.environ['YAHOO_APIID']
weather_key = os.environ['WEATHERKEY']

intents = discord.Intents.all()
client = discord.Client(intents=intents)

#Bootmsg-console
@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

#ﾎｼﾏﾁｰ!!
@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('ﾎｼﾏﾁｰ!!') :
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

#今日も一日
'''
tenkimsg = None
rssurlOkayama = "https://rss-weather.yahoo.co.jp/rss/days/6610.xml"
tenkiURLOkayama = "https://weather.yahoo.co.jp/weather/33/6610/33202.html"
rssurlFukuyama = "https://rss-weather.yahoo.co.jp/rss/days/6710.xml"
tenkiURLFukuyama = "https://weather.yahoo.co.jp/weather/34/6710/34207.html"

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if message.content.startswith('今日も一日!'):

        await message.channel.send('')
'''

#ウェルカムメッセージのようなもの
'''
@client.event
async def on_member_join(member):
    await 
'''

client.run(token)