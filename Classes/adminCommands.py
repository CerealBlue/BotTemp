import discord
from discord.ext import commands
from Servers import *




class administratorModeration:
	def __init__(self, bot):
		self.botAdmin = bot
		self.server = serversData()
		self.server.updateServ

	@commands.command(name = 'warning',
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
				"\nIf you choose 6, you must type the reason after the bot asks you for the reason.",
			brief=
				"Sends a warning in a private message to a particular user",
			pass_context=True,
			hidden=True)
	async def warning(ctx):
		roles = []

		for role in ctx.message.author.roles:
			roles.append(str(role))

		if (self.checkAdmin(roles)):
			await self.botAdmin.send_message(ctx.message.channel, "```ENTER USERNAME:\t\t\tDo not @userName```")
			userToBeWarned = await self.botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

			
						
		
		#alertMe(reason)
		return -1
		
	def checkAdmin(listOfRoles):
		for role in listOfRoles:
			if ("Admin" in roles) or ("admin" in roles):
				return 1
		return 0









"""@client.command(name='greetings',
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
""""
