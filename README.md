# Discord-D20Bot
The public source code of my Discord dicebot written in Python

## Using
This bot requires that you have a proper Discord bot account through https://discordapp.com/developers/applications/me
 
 - Python 3.5.1 + additional libraries:
  - https://github.com/Rapptz/discord.py
  - https://github.com/seatgeek/fuzzywuzzy
 - Git (You're on Github for christ sakes)
 - A Discord account to use the bot

 When you have python installed you'll need to install the following libraries using in your console:

`pip3 install python-Levenshtein`

`pip3 install git+https://github.com/Rapptz/discord.py@async`
 
Now you're almost ready, before running the bot script you will need to modify the [`token`](https://github.com/RowenStipe/Discord-D20Bot/blob/master/diceroll.py#L28) value to match the your bot account token

Your bot is now ready to start using discord.

To get your bot onto different servers you'll need proper server permissions, and the `Client ID` on your bot's application page then go to `https://discordapp.com/oauth2/authorize?&client_id={Your bot's Client ID here}&scope=bot` to direct it to servers. This URL can be shared to bring your bot to other servers.

If you don't want to run a bot of your own you can invite my D20Bot with https://discordapp.com/oauth2/authorize?&client_id=169068074010542080&scope=bot

I can usually be found here on Discord: [Charisma Bonus](https://discord.gg/AChmBdp)
