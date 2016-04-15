#!/usr/bin/env python3
""" Discord D20Bot  
    Copyright (C) 2016  RowenStipe

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import discord
from discord.ext import commands

from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import random

# Compairitor string for dice
cdice = '000d000'
# Token to change for bot
token = '1YOUR2BOT3TOKEN5HERE4'

description = "A more advanced dice rolling bot."

bot = commands.Bot(description=description)

@bot.event
async def on_ready():
    print('Loading the dice for:')
    print(bot.user.name)
    print(bot.user.id)
    print('~~~~~~~~~~~~~~~~~~~~~~')
    
    
@bot.event
async def on_message(message):
    # start Dice magic
    msg = message.content.split(' ')

    if message.content.startswith('$help'):
        await bot.send_message(message.channel,'To make me roll dice for you simply type: \n `[#of dice]d[# Dice] [± Modifier] [Optional Message here]` \n `1d20 +8 Performance Check` \n To have me decide something for your lazy self: \n `$decide This or That or This thing or That guy over there` using `or` to separate the choices \n\n My source code: https://github.com/RowenStipe/Discord-D20Bot')
    
    if message.content.startswith('$decide'):
        
        decide_str = message.content.replace('$decide ', '')
        decide_lst = decide_str.split('or')
        rng = random.choice(decide_lst)
        decision = rng.strip()
        
        await bot.send_message(message.channel, '{0.author.mention} out of the choices between: *{1}* \n The decision is: *{2}*'.format(message, decide_str, decision))

    # Detect if Dice formula is given with out command: Basic
    if fuzz.ratio(cdice, msg[0]) >= 18:
        # Check if only dice is given
        if len(msg) < 2:
            msg.insert(1, '0')
            msg.insert(2, ' ')
        # Check if missing optional message
        if len(msg) < 3:
            msg.insert(2, ' ')
        mod = msg[1].replace("+", "")
        psay = ' '.join(msg[2:])
        try:
            rollt, maxn = map(int, msg[0].split('d'))
        except ValueError:
            pass
        
        try:
            i = 0
            rolled = []
            while (i < rollt):
                rng = random.randint(1, maxn)
                rolled.append(rng)
                print('Rolled: {0}'.format(rolled))
                i = i + 1
            rtotal = ' '.join(str(rolled))
            total = sum(rolled) + int(mod)
            sayr = '**{0.author.mention} Rolled**_(d{1})_ **:** `{2} + {3}` _{4}_ \nTotal: `{5}`'.format(message, maxn, rtotal, mod, psay, total)
            await bot.send_message(message.channel, sayr)
        except UnboundLocalError:
            pass
            
bot.run(token)