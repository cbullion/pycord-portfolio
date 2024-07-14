# SETUP

import asyncio
import datetime
import discord

botIntents = discord.Intents.all()
botPrefix = "!"
botColor = 0xFFFFFF  # Default color of the embeds. 
bot = commands.Bot(command_prefix=botPrefix, intents=botIntents)


# GENERAL MESSAGE POOL
# These messages will always be in the pool of potential messages.
  
message_pool = [
	"MESSAGE 1",
	"MESSAGE 2",
	"MESSAGE 3"
]


  
# SEASONAL MESSAGE POOL
# These messages will only be added to the pool of potential messages during their respective seasons. 
  
seasonal_messages = {
	"spring": ["MESSAGE 1", "MESSAGE 2", "MESSAGE 3"],
	"summer": ["MESSAGE 1", "MESSAGE 2", "MESSAGE 3"],
	"autumn": ["MESSAGE 1", "MESSAGE 2", "MESSAGE 3"],
	"winter": ["MESSAGE 1", "MESSAGE 2", "MESSAGE 3"],
}



# DAY-OF-THE-WEEK MESSAGE POOL
# These messages will only be added to the pool of potential messages during the matching day of the week.
  
day_messages = {
	# Monday
  0: ["MESSAGE 1"],
	# Tuesday
  1: ["MESSAGE 1"],
	# Wednesday
  2: ["MESSAGE 1"],
	# Thursday
  3: ["MESSAGE 1"],
	# Friday
  4: ["MESSAGE 1"],
	# Saturday
  5: ["MESSAGE 1"],
	# Sunday
  6: ["MESSAGE 1"],
}



# HOLIDAY MESSAGES
# This pool contains dates and messages for holidays. Will always play the matching message on a holiday. 
  
holidays = {
	"01-01": "NEW YEARS MESSAGE",
	"12-25": "CHRISTMAS MESSAGE",
}


# MAIN CODE

@tasks.loop(minutes=15)
async def check_announcement():

	channel_id = ################  # Insert channel ID where you want the messages to be sent. 
	channel = bot.get_channel(channel_id)

	while True:
		# Calculates and schedules the message.
		now = datetime.datetime.now()
		goal_time = datetime.datetime(now.year, now.month, now.day, 12, 00)  # The time you want the messages to send.
		if now >= goal_time:
			goal_time = goal_time + datetime.timedelta(days=1)
		delay = (goal_time - now).total_seconds()

		await asyncio.sleep(delay)  # Sleeps until it's time to send the message.

		today = datetime.date.today()
		today_key = today.strftime("%m-%d")

		if today_key in holidays:
			holiday_messages = holidays[today_key]
			embed = discord.Embed(title="TODAY'S MESSAGE IS:" , description=f"{holiday_messages}", color=botColor)
			await channel.send(embed=embed)
		else:
			current_pool = message_pool
			# Adds seasonal messages
			current_season = get_season(today)
			if current_season in seasonal_messages:
				current_pool.extend(seasonal_messages[current_season])
			# Adds day of the week messages
			day_of_week = today.weekday()
			print(day_of_week)
			if day_of_week in day_messages:
				current_pool.extend(day_messages[day_of_week])
			# Select a random message from the pool and send it
			selected_message = random.choice(current_pool)
			embed = discord.Embed(title="TODAY'S MESSAGE IS:" , description=f"{selected_message}", color=botColor)
			await channel.send(embed=embed)

def get_season(date):
	# Determine the season based on the month of the date
	month = date.month
	if 3 <= month <= 5:
		return "spring"
	elif 6 <= month <= 8:
		return "summer"
	elif 9 <= month <= 11:
		return "autumn"
	else:
		return "winter"
