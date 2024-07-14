# Sends a message to a designated logging channel whenever the bot goes online. 

import discord

botIntents = discord.Intents.all()
botPrefix = "!"
botColor = 0xFFFFFF  # Default color of the embeds. 
bot = commands.Bot(command_prefix=botPrefix, intents=botIntents)

logChannel = #################  # Insert the channel ID of your logging channel

@bot.event
async def on_ready():
	onlineEmbed=discord.Embed(description="BOT IS ONLINE.", color=botColor)
	await bot.get_channel(logChannel).send(embed=onlineEmbed)
