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

import random

# Token to change for bot
token = '1YOUR2BOT3TOKEN5HERE4'

description = "A more advanced dice rolling bot."

bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    print('Loading the dice for:')
    print(bot.user.name)
    print(bot.user.id)
    print('~~~~~~~~~~~~~~~~~~~~~~')
    
    
@bot.event
async def on_message(message):
    # Dectection for dice later on
    msg = message.content.split(' ')

    # $help command
    if message.content.startswith('$help'):
        await bot.send_message(message.channel,'To make me roll dice for you simply type:\n`$r [#of dice MAX:255]d[# Dice MAX:10000] [± Modifier] [Optional Message here]`\nor\n`1d20 +8 Performance Check`\n\nTo have me decide something for your lazy self:\n`$decide This or That or This thing or That guy over there` using `or` to separate the choices\n\nMy source code: `https://github.com/RowenStipe/Discord-D20Bot`')
    
    # Make a decision
    if message.content.startswith('$decide'):
        decide_str = message.content.replace('$decide ', '') # Keep mostly raw string for later
        decide_lst = decide_str.split('or') # List decisions up
        rng = random.choice(decide_lst) # ???(Random choice from list)
        decision = rng.strip() # Profit!(Decide something)
        
        await bot.send_message(message.channel, '{0.author.mention} out of the choices between: *{1}* \n The decision is: *{2}*'.format(message, decide_str, decision))

    # Detect if 1d20 formula is given
	if message.content.startswith('$r') or message.content.startswith('$roll'):
        rollt = 0
        maxn = 0
        # Check if only dice is given to toss
        if len(msg) < 3:
            msg.insert(2, '0')
            msg.insert(3, ' ')
        # Check if missing optional message string
        if len(msg) < 4:
            msg.insert(3, ' ')
        mod = msg[2].replace("+", "") # Remove '+' in: 1d20 +4 type strings (Returns 4)
        psay = ' '.join(msg[3:]) # Compiles optional message, or what ever the cat hit afterwards
        try:
            rollt, maxn = map(int, msg[1].split('d')) # Decide what and how many times to roll
        except ValueError:
            pass    
        try:
            if rollt > 255:
                await bot.send_message(message.channel, '**{0.author.mention}** You want to roll too many dice!'.format(message))
                valueerror = 'Too many Dice'
                raise ValueError('Too mand dice')
            if maxn > 10000:
                await bot.send_message(message.channel, '**{0.author.mention}** I don\'t have that high of dice to roll!'.format(message))
                valueerror = 'Too high of dice'
                raise ValueError('To high of dice')
        except ValueError:
            print(valueerror)
        else:
            try:
                i = 0
                rolled = [] # List of rolls
                while (i < rollt):
                    rng = random.randint(1, maxn)
                    rolled.append(rng)
                    i = i + 1
                total = sum(rolled) + int(mod) # Decide the total ammout rolled
            
                sayr = '**{0.author.mention} Rolled**_(d{1})_ **:** `{2}` + {3} _{4}_ \nTotal: `{5}`'.format(message, maxn, rolled, mod, psay, total) #  Markdown formatted string to say
                await bot.send_message(message.channel, sayr)
            except ValueError:
                pass
        finally:
            pass
            
bot.run(token)