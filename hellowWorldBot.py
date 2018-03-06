#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 12:09:47 2018

@author: syou
"""

import discord
import random
import os
from flask import Flask

app = Flask(__name__)
app.debug = True

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

   
@client.event
async def on_message(message):
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
            
    elif message.content.startswith("えらんげる"):
        erangelList = ["リポブカ","ザラキ","ポチンキ","Severny","スクール","病院","すたるばー",
                       "ミリべ","射撃場","やすなや","ロズホック","ミルタ","マンション","ミルタパワー",
                       "シェルター","水の都","遺跡","フェリー乗り場","ジョージ北","ジョージ南","ジョージコンテナ",
                       "プリモスク","ノヴォ","学校横マンション"]
        discentPlace = random.choice(erangelList)
        await client.send_message(message.channel, discentPlace)
    
    elif message.content.startswith("みらまー"):
        miramarList = ["La Cobreria","Torre Ahumada","Compo Militar","Tierra Bronca",
                       "Cruz del Valle","Water Treatment","Crater Fields","El Pozo",
                       "SanMartin","Hacienda del Patron","Graveyard,Minas Generales",
                       "Junkyard","Monte Nuevo","Pecado","Impala","Chumacera","Los Leones",
                       "PuertoParaiso","Valle del Mar","Prison,Minas del Sur","Los Higos",
                       "右にある島二つ","Los Leonesの下にaarrrsfdjioafjwoeisある田舎"]
        discentPlaceM = random.choice(miramarList)
        await client.send_message(message.channel, discentPlaceM)
        
    elif message.content.startswith("すかいりむ"):
        await client.send_message(message.channel, "PUBGしろ")
        
        
        

# token にDiscordのデベロッパサイトで取得したトークンを入れてください
client.run("NDE5NzQwOTA2MDQ4OTc4OTQ0.DX5FvQ.Kgm1ykVzdRdMUQGmyVadnsLFS6w")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
