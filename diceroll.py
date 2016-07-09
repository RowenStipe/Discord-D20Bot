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
import dice.roll as roll
import sys

# Token to change for bot
token = 'MTc5NjAzMTE4OTUzMDcwNTkz.CmHVjQ.kH8_8SvsM1f6oN4PlIpBWUWN9dc'

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
    # For Dice later on
    msg = message.content.split(' ')

    # $help command
    if message.content.startswith('$help'):
        await bot.send_message(message.channel,'To make me roll dice for you simply type:\n`$r [#of dice MAX:255]d[# Dice MAX:10000] [± Modifier] [Optional Message here]`\nor\n`1d20 +8 Performance Check`\nAdd a `!` to the end of your dice fore exploding dice. e.g. `3d8!`\n\nTo have me decide something for your lazy self:\n`$decide This or That or This thing or That guy over there` using `or` to separate the choices\n\n`$statgen` To roll 6 random stats.\n\n`$8ball Question here` to have me shake the magic 8-ball\n\n\nMy source code: `https://github.com/RowenStipe/Discord-D20Bot`')
    
    # Make a decision
    if message.content.startswith('$decide'):
        decide_str = message.content.replace('$decide ', '') # Keep mostly raw string for later
        decide_lst = decide_str.split('or') # List decisions up
        rng = random.choice(decide_lst) # ???(Random choice from list)
        decision = rng.strip() # Profit!(Decide something)
        
        await bot.send_message(message.channel, '{0.author.mention} out of the choices between: *{1}* \n The decision is: *{2}*'.format(message, decide_str, decision))

    # The magic 8ball
    if message.content.startswith('$8ball'):
        eightball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes, definitely.", "You may rely on it.", "As I see it? Yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy try again.", "Ask later.", "Better not tell you now.", "Cannot predict now.","Concentrate and ask again.", "Do not count on it.", "My reply is~ no.", "My source code says-- No.", "Outlook does not look good.", "Very doubtful.", "Fuck off.", "42"]
        rng = random.choice(eightball)
        decision = rng.strip()
        question = ' '.join(msg[1:]) # The question

        await bot.send_message(message.channel, '{0.author.mention} You asked: {1} \n I\'ve shaken the ball and it says: \n `{2}`'.format(message, question, decision))

    # Generate stats
    if message.content.startswith('$statgen'):
        stats = []
        i = 0
        while (i < 6):
            ii = 0
            gen = []
            while (ii < 4):
                rng = random.randint(1, 6)
                gen.append(rng)
                ii = ii +1
            gen.remove(min(gen))
            stats.append(sum(gen))
            i = i + 1
        
        await bot.send_message(message.channel, '**{0.author.mention}** Your generated stats are: \n `{1}`'.format(message, stats))

    #Dev Command
    if message.content.startswith('$test'):
        del msg[0] #remove command
        sdm = roll.sortmsg(msg)
        # await bot.send_message(message.channel, 'Sorted roll is:\n```Dice to roll: \n {0.d2r} \n Modifiers: \n{0.mod} \n Player Message \n {0.pmsg}```'.format(sdm))
        rolledd = roll.dice(sdm.d2r)
        totalcalc = roll.calc(rolledd.rn, sdm.mod)
        rolled_lst = rolledd.rd
        rolled_str = ' \n '.join(map(str, rolled_lst))
        await bot.send_message(message.channel, '{3.author.mention} I rolled the dice for you:\n ```py\nRolled Dice:\n {0}\nMods applied:\n {1.mod}\n\nCalculated Total [ {2.ct} ]```\n{1.pmsg}'.format(rolled_str, sdm, totalcalc, message))

bot.run(token)