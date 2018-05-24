import discord
from discord.ext import commands
#from Servers import *



class administratorModeration:
	def __init__(self, bot):
		self.botAdmin = bot

	@botAdmin.command(name = 'warning',
-					description=
-						"Syntax:\n\n ++warning\nENTER ID:\n<IDNumber>\nReason Number:\n<Reason Number>\n\nEx:\n++warning\nENTER ID:\n47293***********3234\nReason Number:\n6"
		-				"\n\nYou get the ID Number by:\nLaptop: Right Click on User. Copy ID. Paste. "
		-				"\nMobile: Long Hold on User. Scroll Down. Copy ID. Paste."
		-				"\n\nSend a private message to the user you want to warn with one of the reasons below:\n"
		-				"\n1. Inappropriate Language"
		-				"\n2. Trolling"
		-				"\n3. Insulting Others"
		-				"\n4. Unnecessary Spam (pictures or repeated attempts to send something over)"
		-				"\n5. Speaking about unnecessary topics"
		-				"\n6. Insulting a Mod/Admin in a non-friendly way"
		-				"\n\n7. Other (Must be specified)"
		-				"\n\nThe bot then asks you which reason. You reply one of the numbers from above."
		-				"\nIf you choose 7, you must type the reason after the bot asks you for the reason.",
		-			brief=
		-				"Sends a warning in a private message to a particular user",
		-			pass_context=True,
		-			hidden=True)
	async def warning(ctx):
        if not ctx.message.author.server_permissions.kick_member:
    		await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
    		return(0)

		await botAdmin.send_message(ctx.message.channel, "```To cancel, type: blue```")
		await botAdmin.send_message(ctx.message.channel, "```ENTER ID:```")
		userToBeWarnedPrim = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
		userToBeWarned = userToBeWarnedPrim.content

		try:
			if (userToBeWarned.lower() == "blue"):
				await botAdmin.send_message(ctx.message.channel, "```WARNING ABORTED```")
				return 0
		except:
			continue

		await botAdmin.send_message(ctx.message.channel, "```REASON NUMBER:```")
		reasonNumber = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		try:
			if (reasonNumber.content.lower() == "blue"):
				await botAdmin.send_message(ctx.message.channel, "```WARNING ABORTED```")
				return 0
		except:
			continue

		reasonToBeSent = ""
		if (int(reasonNumber.content) == 7):
			await botAdmin.send_message(ctx.message.channel, "```ENTER REASON:```")
			reasonToBeSentMsg = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

			try:
				if (reasonToBeSentMsg.content.lower() == "blue"):
					await botAdmin.send_message(ctx.message.channel, "```WARNING ABORTED```")
					return 0
			except:
				continue


			reasonToBeSent = reasonToBeSentMsg.content


		adminServer = botAdmin.get_server(ctx.message.server.id)
		userToBeWarnedID = adminServer.get_member(userToBeWarned)

		reaNum = int(reasonNumber.content)
		strikeCount = 0
		#data = getMemberData(userToBeWarned, serverID)

		#if (data != -1):
			#strikeCount = len(data["strikes"])

		embedTitle = "Infraction"
		embedColour = discord.Colour.red()
		embedDesc = []
		embedDesc.append("__**Infraction**__\n")
		embedDesc.append("This is a Formal Infraction through a strike.\nIf you think your infraction is undoubtedly unjustified, please **do not** post about it in a public channel but take it up with an administrator.\n")
		embedDesc.append("\n\n**__REASON:__**\n")

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

		sendEmbed = discord.Embed(title = embedTitle, description = ''.join(embedDesc), colour = embedColour)
		sendEmbed.add_field(name = "Strike Given:", value = str(1))
		sendEmbed.add_field(name = "Strike Count:", value = str(strikeCount)+"/3")

		await botAdmin.send_message(ctx.message.channel, "```Warned User:\t"+str(userToBeWarned)+"\nReason Number:\t"+str(reaNum)+"\nReason Sent:\t"+str(reasonToBeSent)+"```")

		warningMSG = []
		warningMSG.append(str(userToBeWarnedID) + "\twarned by\t" + str(ctx.message.author.id) + "\tat\t" + str(datetime.datetime.now()) + "\tfor\t")
		warningMSG.append("Reason Number # " + str(reaNum))

		if (reaNum == 7):
			warningMSG.append(":\t" + reasonToBeSent)

		#writeMemberData(memberID = userToBeWarnedID, serverID = ctx.message.server.id, warning = ''.join(warningMSG))
		#checkMemberOfDangers

	@botAdmin.command(name = 'strike',
-					description=
-						"Syntax:\n\n ++strike\nENTER ID:\n<IDNumber>\nReason Number:\n<Reason Number>\n\nEx:\n++strike\nENTER ID:\n47293***********3234\nReason Number:\n6"
		-				"\n\nYou get the ID Number by:\nLaptop: Right Click on User. Copy ID. Paste. "
		-				"\nMobile: Long Hold on User. Scroll Down. Copy ID. Paste."
		-				"\n\nSend a private message to the user you want to warn with one of the reasons below:\n"
		-				"\n1. Inappropriate Language"
		-				"\n2. Trolling"
		-				"\n3. Insulting Others"
		-				"\n4. Unnecessary Spam (pictures or repeated attempts to send something over)"
		-				"\n5. Speaking about unnecessary topics"
		-				"\n6. Insulting a Mod/Admin in a non-friendly way"
		-				"\n\n7. Other (Must be specified)"
		-				"\n\nThe bot then asks you which reason. You reply one of the numbers from above."
		-				"\nIf you choose 7, you must type the reason after the bot asks you for the reason.",
		-			brief=
		-				"Sends a strike in a private message to a particular user",
		-			pass_context=True,
		-			hidden=True)
	async def strike(ctx):
        if not ctx.message.author.server_permissions.kick_member:
    		await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
    		return(0)

		await botAdmin.send_message(ctx.message.channel, "```TO CANCEL, TYPE: blue```")
		await botAdmin.send_message(ctx.message.channel, "```ENTER ID:```"-)
		userToBeStrikedPrim = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
		userToBeStriked = userToBeStrikedPrim.content

		try:
			if (userToBeStriked.lower() == "blue"):
				await botAdmin.send_message(ctx.message.channel, "```STRIKE ABORTED```")
				return 0
		except:
			continue

		await botAdmin.send_message(ctx.message.channel, "```REASON NUMBER:```")
		reasonNumber = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		try:
			if (reasonNumber.content.lower() == "blue"):
				await botAdmin.send_message(ctx.message.channel, "```STRIKE ABORTED```")
				return 0
		except:
			continue

		reasonToBeSent = ""
		if (int(reasonNumber.content) == 7):
			await botAdmin.send_message(ctx.message.channel, "```ENTER REASON:```")
			reasonToBeSentMsg = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
			reasonToBeSent = reasonToBeSentMsg.content

			try:
				if (reasonToBeSent.content.lower() == "blue"):
					await botAdmin.send_message(ctx.message.channel, "```STRIKE ABORTED```")
					return 0
				except:
					continue



		adminServer = botAdmin.get_server(ctx.message.server.id)
		userToBeStrikedID = adminServer.get_member(userToBeWarned)

		reaNum = int(reasonNumber.content)
		strikeCount = 1
		#data = getMemberData(userToBeWarned, serverID)

		#if (data != -1):
			#strikeCount = len(data["strikes"]) + 1

		embedTitle = "Infraction"
		embedColour = discord.Colour.dark_red()
		embedDesc = []
		embedDesc.append("__**Infraction**__\n")
		embedDesc.append("This is a Formal Infraction through a Strike.\nIf you think your infraction is undoubtedly unjustified, please **do not** post about it in a public channel but take it up with an administrator.\n")
		embedDesc.append("\n\n**__REASON:__**\n")

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

		sendEmbed = discord.Embed(title = embedTitle, description = ''.join(embedDesc), colour = embedColour)
		sendEmbed.add_field(name = "Strike Given:", value = str(1))
		sendEmbed.add_field(name = "Strike Count:", value = str(strikeCount))

		await botAdmin.send_message(userToBeStrikedID, embed = sendEmbed)

		await botAdmin.send_message(ctx.message.channel, "```Striked User:\t"+str(userToBeWarned)+"\nReason Number:\t"+str(reaNum)+"\nReason Sent:\t"+str(reasonToBeSent)+"```")

		strikedMSG = []
		strikedMSG.append(str(userToBeStrikedID) + "\twarned by\t" + str(ctx.message.author.id) + "\tat\t" + str(datetime.datetime.now()) + "\tfor\t")
		strikedMSG.append("Reason Number # " + str(reaNum))

		if (reaNum == 7):
			strikedMSG.append(":\t" + reasonToBeSent)

		#writeMemberData(memberID = userToBeWarnedID, serverID = ctx.message.server.id, strike = ''.join(strikedMSG))
		#checkMember'sStrikes=3  and them kick them out.

	@botAdmin.command(name="authAdminBotControlChannel",
						description=
						"This command authorizes a channel so that admin commands can work.\n\nNote:\tThe Authorizer must be an Admin.\n"
						"\nSyntax:"
						"\n++AuthChannel"
						"\nTYPE blue TO CONFIRM"
						"\nblue",
						brief="Authorizes an Admin Channel",
						hidden=True,
						pass_context=True)
	async def authAdminBotControlChannel(ctx):
        if not ctx.message.author.server_permissions.administrator:
    		await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
    		return(0)

		await botAdmin.send_message(ctx.message.channel, "```TYPE blue TO CONFIRM```")
		authChannelReplyMsg = await botAdmin.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

		if (authChannelReplyMsg.content.lower() == "blue"):
			if (setAdminBotControlChannel(ctx.message.channel.id))
				await botAdmin.send_message(ctx.message.channel, "```CHANNEL AUTHORIZED```")
			else:
				await botAdmin.send_message(ctx.message.channel, "```FAILED```")
		else:
			await botAdmin.send_message(ctx.message.channel, "```CHANNEL AUTHORIZING ABORTED```")

	@botAdmin.command(name="setPollChannel",
						description="This command sets the poll channel."
						"\n\nNotes:"
						"\n\t>The setter must be an Admin."
						"\n\t>The target channel is the channel you type this command into."
						"\n\t>Only one pollChannel can be set. Everytime you use this command, the latest channel where you used it will be the target poll channel"
						"\n\nIMPORTANT NOTE:"
						"\n\t>The Poll Channel must have all permissions set to \"X\" for this channel to work effectively",
						brief="Set the target of your poll channel",
						hidden=True,
						pass_context=True)
	async def setPollChannel(ctx):
		if not ctx.message.author.server_permissions.administrator:
    		await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
    		return(0)

		allMessages = []
		allMessages.append(ctx.message)

		setPollChannel(ctx.message.server.id, ctx.message.channel.id)

		completedMsg = await botAdmin.send_message(ctx.message.channel, "```COMPLETED```")
		allMessages.append(completedMsg)

		await asyncio.sleep(5)
		await botAdmin.delete_messages(allMessages)

	@botAdmin.command(name="echo",
						description="This command lets the bot to write something on your behalf to a channel."
						"\n\nNotes:"
						"\n\t>The echoer must be an admin"
						"\n\t>You must use the channel ID to make use of this channel"
						"\n\nSyntax:"
						"\n++echo xxxx_channelID_xxxx message"
						"\n\nExample:"
						"\n++echo 1234567898765432 Life is a pain.",
						brief="Can send a message via the bot to a channel",
						pass_context=True,
						hidden=True)
	async def echo(ctx):
		if not ctx.message.author.server_permissions.administrator:
			await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
			return(0)

		#checkAuthAdminChannel
