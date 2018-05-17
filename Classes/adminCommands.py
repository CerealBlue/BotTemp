import discord
from discord.ext import commands



class administratorModeration:
	async def warning(ctx):
		roles = []
		bot = client

		for role in ctx.message.author.roles:
			roles.append(str(role))

		if (checkAdmin(roles) == 0):
			#alertMe(reason)
			return (-1)

		await bot.send_message(ctx.message.channel, "```ENTER ID:\n\nDo not @userName```")
		userToBeWarnedPrim = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
		userToBeWarned = userToBeWarnedPrim.content	

		await bot.send_message(ctx.message.channel, "```Reason Number:```")
		reasonNumber = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		reasonToBeSent = ""
		if (int(reasonNumber.content) == 7):
			await bot.send_message(ctx.message.channel, "```Enter Reason:```")
			reasonToBeSentMsg = await bot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
			reasonToBeSent = reasonToBeSentMsg.content


		adminServer = client.get_server(ctx.message.server.id)
		userToBeWarnedID = adminServer.get_member(userToBeWarned)

		reaNum = int(reasonNumber.content)
		strikeCount = 0
		#data = getMemberData(userToBeWarned, serverID)

		#if (data != -1):
			#strikeCount = len(data["strikes"])

		embedTitle = "Infraction"
		embedColour = discord.Colour.gold()
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
			await bot.send_message(ctx.message.channel, "```FAILED ERROR# WARN01```")

		#try:
		await bot.send_message(userToBeWarnedID, embed = sendEmbed)
		#except:
		#	await bot.send_message(ctx.message.channel, "```FAILED ERROR# WARN02```")

		#await bot.send_message(ctx.message.channel, "```Warned User:\t"+str(userToBeWarned)+"\nReason Number:\t"+str(reaNum)+"\nReason Sent:\t"+str(reasonToBeSent)+"```")

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
