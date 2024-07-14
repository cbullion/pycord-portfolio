# This code searches an index column on a set Google Sheet and returns whether or not the entered primary key is present.

import discord
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

botIntents = discord.Intents.all()
botPrefix = "!"
botColor = 0xFFFFFF  # Default color of the embeds. 
botGuild = 0000000000000000000  # Replace with server ID number. 
bot = commands.Bot(command_prefix=botPrefix, intents=botIntents)

# GOOGLE API SETUP
apiScope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
apiKey = PUTKEYHERE
googleSheet = gspread.authorize(apiKey)


@bot.slash_command(name="numcheck", description='Checks if a number is free', guild_ids=[botGuild])
async def search(ctx,
		query: Option(str, "Enter the number.", required=True),
): 

  WKS = googleSheet.open("SHEET NAME").worksheet("TAB NAME")
  DATA = WKS.get_all_values()
  HEADERS = DATA.pop(0)
  DF = pd.DataFrame(DATA, columns=HEADERS)

  if query in DF['NUMBER'].values:  # Rename 'NUMBER' to the column name containing your primary key.
    await ctx.respond(f"Number `{query}` is taken.", ephemeral = True)
  else:
    await ctx.respond(f"Number `{query}` is available.", ephemeral = True)
