#2018-04-13 11:23:13

from discord.ext.commands import Bot
from discord import Game
import datetime
import sys
import asyncio
from random import choice
#import praw
from subprocess import call

from classes.Servers import * as serversData

#sys.path.append("/home/CerealBlue/Desktop/Discord/SuperUserBot/MemeTaker_Bot/")

#from mt_b import mt_b_start as memesteal

TOKEN = "NDM0MDI3NzE2Nzk1NDMyOTYx.DcdETQ.rdsieJCA2pCYoz68o481J1BvgXg"

BOT_PREFIX = ("?", "!", "++")

client = Bot(command_prefix=BOT_PREFIX)

"""class Lists:
	def __init__(self):
		self.idList = []

	def addId(self, Id):
		self.idList.append(Id)

	def IdList(self, Id):
		if Id in idList:
			return 1
		return 0



	def returnServerInfo(self):
		lis = []
		lis.append( str( "```Bot Calls From Servers```" ) )
		for i in self.servo:
			lis.append( str( "`  "+str(self.servo[i][0])+"  `:\t" ) )
			lis.append( str( "`  "+str(self.servo[i][1])+"  `" ) )
			lis.append("\n")
		lis = ''.join(lis)
		return (lis)

def TrustedPeople:
	def __init__(self):
		self.users = []
		with open("TrustedUsers", 'r') as FileObj:
			self.users.append(FileObj.getline())

	def addUser(self, user):


"""


#suBot = serversData()


@client.command(name='greetings',
                description="This command makes SuperUserBot greet you.",
                brief="Bot Greets",
		aliases=['hey','hi','hello', 'sup', 'wassup'],
		pass_context = True)
async def greet(context):
	#suBot.addCall(context.message.server.id)
	greeters = [
		"Wassup,",
	        "Salutations",
	        "Hello from the Cloud!",
	        "Hello! I stay in a Raspberry Pi! It's doesn't taste like a Pie though :( ...",
	        "My Creator (The great BlueCereal) has taught me to greet people (I'm anti-social, btw). Here goes... ~~Gretings~~ ~~Greatthings~~ \n\nGreetings,"]
	await client.say(choice(greeters) + " " + context.message.author.mention + ".")


@client.command(name='time',
                description=
                "This command displays the date and time in:"
                "\n\t>YYYY-MM-DD HH:MM:SS:MS"
                "\n\t>Current Year"
                "\n\t>Current Month"
                "\n\t>WeekNumber"
                "\n\t>WeekdayNumber"
                "\n\t>Day of the Year"
                "\n\t>Day of the Month"
                "\n\t>Day of the Week"
                "\n\nAlso, why are you this lazy to not look at your phone's time?",
                brief="Time Displayer",
                aliases=['date', 'day'],
		pass_context = True)
async def timeDisplay(context):
	#suBot.addCall(context.message.server.id)
	await client.say("Time:\n"
                    "```"+str(datetime.datetime.now())+"```\n"
                    "Current year: \t`" +     str(datetime.date.today().strftime("%Y")) + "`\n"
                    "Current Month: \t`" +    str(datetime.date.today().strftime("%B")) + "`\n"
                    "WeekNumber \t`" +        str(datetime.date.today().strftime("%W")) + "`\n"
                    "WeekdayNumber: \t`" +    str(datetime.date.today().strftime("%w")) + "`\n"
                    "Day of the Year: \t`" +  str(datetime.date.today().strftime("%j")) + "`\n"
                    "Day of the Month: \t`" + str(datetime.date.today().strftime("%d")) + "`\n"
                    "Day of the Week: \t`" +  str(datetime.date.today().strftime("%A")) + "`\n"
                    )


"""@client.command(name='logoutBlue',
		pass_context=True,
		hidden=True)
async def logoutBlue(context):
	print (type(context.message.author.id))
	if (suBot.isMe(context.message.author.id)):
		pingedServ = client.get_server(context.message.server.id)
		me = pingedServ.get_member(suBot.myId())
		senderMsg = "```Request to Logout at:\t"+str(datetime.datetime.now())+"\n\nType Y to continue (5 seconds):```"
		await client.send_message(me, senderMsg)

		""def check(msg):
			if msg.content == 'Logout':
				print ('ya')
				return 1
			print ('no')
			return 0""

		confirmMsg = await client.wait_for_message(timeout = 15, author = context.message.author,channel=me, content='Logout')
		print (confirmMsg)
		""if confirmMsg.content == 'Y':
			print ('y')
		else:
			print ("no")
		"""
@client.command(name='test',
		description=
			"Syntax: ++warning\nENTER USERNAME:\nUserName\n\nEx:\n++warning\nENTER USERNAME:\nBlueCereal"
			"\n\nDo NOT @UserName HERE"
			"\n\nSend a private message to the user you want to warn with one of the reasons below:\n"
			"\n1. Inappropriate Language"
			"\n2. Trolling"
			"\n3. Insulting Others"
			"\n4. Unnecessary Spam"
			"\n5. Insulting a Mod/Admin in a non-friendly way"
			"\n6. Other (Must be specified)"
			"\n\nThe bot then asks you which reason. You reply one of the numbers from above."
			"\nIf you choose 6, you must type the reason after it asks you for the reason.",
		brief="Pm a dude",
		pass_context=True,
		hidden=True)
async def test(ctx):
	print (str(ctx.message.author.roles[0]))
	for i in ctx.message.author.roles:
		print (str(i))



@client.command(name='joke',
                description="Do you want a joke? Well get ready for these jokes!\n\nType Specifiers: <none> <dark>\n\nExample:\n!joke\t!joke dark",
                brief="Joke Sender",
		pass_context = True)
async def joke(context):
	#suBot.addCall(context.message.server.id)
	msg = context.message.content
	subR = "jokes"
	if "dark" in msg:
		await client.say("Dark joke, huh? Let's do it")
		subR = "darkjokes"
	else:
		await client.say("Wait for one sec")


@client.command(name='callsMade',
		description='Bot Creator Only',
		brief='Bot Creator Only',
		pass_context=True,
		hidden=True)
async def callsMade(context):
	#suBot.addCall(context.message.server.id)

	"""if (suBot.isMe(context.message.author.id)):
		pingedServ = client.get_server(context.message.server.id)
		me = pingedServ.get_member(suBot.myId())
		senderMsg = suBot.returnServerInfo()
		await client.send_message(me, senderMsg)


	else:
		print ("no")
"""
@client.command(name='itsshit',
		description='When someone asks you their opinion, and it\'s shit. You send them this.',
		brief='ItsShit Meme',
		pass_context=True)
async def itsshit(context):
	await client.send_file(context.message.channel, "ReactionReplies/ItsShit.jpg", filename="ItsShit.jpg", content="```It's Shit.```")


@client.command(name='addimage',
		pass_context=True)
async def checkat(context):
	#print (context.message.attachments)
	print ("Adding image")
	await client.send_message(context.message.channel, "Send Me a Img")
	msg = await client.wait_for_message(author=context.message.author, channel=context.message.channel)
	#print (msg.attachments)
	url = (msg.attachments[0]['url'])
	if ".jpg" in url:
		call(['wget','-O', 'yo/foo.jpg', str(url) ])
		await client.send_message(context.message.channel, "Col. Done: sending now")
		await client.send_file(context.message.channel, "yo/foo.jpg", filename="foo2.jpg", content="Yo")

	elif ".png" in url:
		call(['wget', '-O', 'yo/foo.png',str(url)])
		await client.send_message(context.message.channel, "Col. Done: sending now")
		await client.send_file(context.message.channel, "yo/foo.png", filename="foo2.png", content="Yo")

	else:
		await client.send_message(context.message.channel, "I need jpg/png")

@client.async_event
async def on_message(message):
	chan = message.channel
	if message.content.startswith('Bot'):
		await client.send_message(message.channel, "hi")
	"""if message.content.startswith('SendMeme'):
		await client.send_message(message.channel, "Wait for a couple of secondz. Pls.\n\nFetching only the best may-mays from:\nReddit!")
		memesteal()

		numberFile = open("MemeTaker_Bot/Number.txt", "r")
		number = int(numberFile.read())
		numberFile.close()

		with open('MemeTaker_Bot/Memes/Meme'+str(number-1)+'.jpeg', 'rb') as f:
			await client.send_file(message.channel, f)
		await client.send_message(message.channel, "Okay?")"""
	#if message.attachments:
	#	print (message.attachments)
	await client.process_commands(message)

@client.event
async def on_ready():
	#print (suBot.retServId(1), type(suBot.retServId(1)))
	#Server = client.get_server(suBot.retServId(1))
	#me = Server.get_member(suBot.myId())

	await client.send_message(me, "```Online at:\t"+str(datetime.datetime.now())+"```")
	await client.change_presence(game=Game(name="with my creator"))
	print ("Logged in as " + client.user.name)




client.run(TOKEN)
