import discord
from discord.ext import commands



class administratorModeration:
	def __init__(self, bot):
		self.botAdmin = bot

	@commands.command(name = 'warning',
			description=
				"Syntax:\n\n ++warning\nENTER ID:\n<IDNumber>\nReason Number:\n<Reason Number>\n\nEx:\n++warning\nENTER ID:\n47293***********3234\nReason Number:\n6"
				"\n\nYou get the ID Number by:\nLaptop: Right Click on User. Copy ID. Paste. "
				"\nMobile: Long Hold on User. Scroll Down. Copy ID. Paste."
				"\n\nSend a private message to the user you want to warn with one of the reasons below:\n"
				"\n1. Inappropriate Language"
				"\n2. Trolling"
				"\n3. Insulting Others"
				"\n4. Unnecessary Spam (pictures or repeated attempts to send something over)"
				"\n5. Speaking about unnecessary topics"
				"\n6. Insulting a Mod/Admin in a non-friendly way"
				"\n\n7. Other (Must be specified)"
				"\n\nThe bot then asks you which reason. You reply one of the numbers from above."
				"\nIf you choose 7, you must type the reason after the bot asks you for the reason.",
			brief=
				"Sends a warning in a private message to a particular user",
			pass_context=True,
			hidden=True)
	async def warning(ctx):
		roles = []

		for role in ctx.message.author.roles:
			roles.append(str(role))

		if (!self.checkAdmin(roles)):
			#alertMe(reason)
			return (-1)

		await self.botAdmin.send_message(ctx.message.channel, "```ENTER ID:\n\nDo not @userName```")
		userToBeWarned = await self.botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		await self.botAdmin.send_message(ctx.message.channel, "```Reason Number:```")
		reasonNumber = await self.botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		reasonToBeSent = ""
		if (int(reasonNumber) == 7):
			await self.botAdmin.send_message(ctx.message.channel, "```Enter Reason:```")
			reasonToBeSent = await self.botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		adminServer = client.get_server(ctx.message.server.id)
		userToBeWarnedID = adminServer.get_member(userToBeWarned)

		reaNum = int(reasonNumber)
		strikeCount = 0
		data = getMemberData(userToBeWarned, serverID)

		if (data != -1):
			strikeCount = len(data["strikes"])

		embedTitle = "Infraction"
		embedColour = discord.Colour(red())
		embedDesc = []
		embedDesc.append("__**Infraction**__\n")
		embedDesc.append("This is a Formal Infraction.\nIf you think your infraction is undoubtedly unjustified, please **do not** post about it in a public channel but take it up with an administrator.\n")
		embedDesc.append("Strikes:\t0\nStrike Count:\t"+str(strikeCount)+"\n\n**__Reason__**:\n")

		if (reaNum == 1):
			reasonToBeSent = "A Moderator had noticed you using Inappropriate Language. Please refrain from using Inappropriate language. We want to maintain this server in a clean way :)."
		if (reaNum == 2):
			reasonToBeSent = "A Moderator had noticed you trolling. We take trolling very seriously and do not want this to happen again. Please refrain from doing this again."
		if (reaNum == 3):
			reasonToBeSent = "A Moderator had noticed you insulting another member. Insulting another member is taken very seriously. Do not insult another member, however primitive they seem to appear."
		if (reaNum == 4):
			reasonToBeSent = "A Moderator had noticed you sending unwanted spam. Please refrain from spamming."
		if (reaNum == 5):
			reasonToBeSent = "A Moderator had noticed you talking about a subject we do not wish to talk about here. Please stop talking about the subject."
		if (reaNum == 6):
			reasonToBeSent = "We appreciate you talking with Admins/Moderators. However, you shouldn't insult an Admin/Moderator. Do not do this again, as it is taken very seriously."
		embedDesc.append(reasonToBeSent)

		try:
			sendEmbed = discord.Embed(title = embedTitle, description = ''.join(embedDesc), colour = embedColour)
		except:
			await self.botAdmin.send_message(ctx.message.channel, "```FAILED ERROR# WARN01```")

		try:
			await self.botAdmin.send_message(userToBeWarnedID, sendEmbed)
		except:
			await self.botAdmin.send_message(ctx.message.channel, "```FAILED ERROR# WARN02")

		await self.botAdmin.send_message(ctx.message.channel, "```Warned User:\t"+str(userToBeWarned)+"\nReason Number:\t"+str(reaNum)+"\nReason Sent:\t"+str(reasonToBeSent))

	def checkAdmin(listOfRoles):
		for role in listOfRoles:
			if "admin" == role.lower():
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
