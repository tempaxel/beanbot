import discord
import configparser
import random
from discord import File

# arakune text
arakuneLines = open('arakuneLines.txt').read().splitlines()


client = discord.Client()
# this lets me know when its logged in


@client.event
async def on_ready():
	print('Logged in as {0.user}'.format(client))

# this says hey when user does !hello and posts a cute pic when !dope


@client.event
async def on_message(message):
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		await message.channel.send('quincy is awesome my good friend')

	if message.content.startswith('!dope'):
		await message.channel.send('https://cdn.discordapp.com/attachments/992156163099607131/1000152522641649705/firefox_CQxZmCFgPy.png')

	if message.content.startswith('!quote'):
		randomQuote = random.choice(arakuneLines)
		await message.channel.send(randomQuote)
	
	if message.content.startswith('!marth'):
		await message.channel.send('https://cdn.discordapp.com/attachments/149270972707504128/213847761974460416/marth_n_chill.jpg')

	if message.content.startswith('!walter'):
		await message.channel.send(file=File("./sDGIJbdns.mp4"))

	if message.content.startswith('!roll'):
		await message.channel.send(random.randint(1, 100))
	
	if message.content.startswith('!8ball'):
		eightBall = random.randint(0, 1)
		if eightBall == 0:
			eightBallResult = "You're gay."
		else:
			eightBallResult = "You're not gay."	
		await message.channel.send(eightBallResult)
		
# importing discord bot token
key = open('TOKEN.txt').read()
client.run(key)
