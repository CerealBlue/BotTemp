"""
Makes A Meme
"""
from PIL import Image, ImageDraw, ImageFont
import discord
from discord.ext import commands

punctuation = ['.', '!', '"', '\'', ',', '-', '?', ';', ' ']
version = '1.0.2'

class memeFormat:
	def __init__(self, memeName, memeLocName, memePicFormat):
		self.data = {}
		self.counter = 0
		self.name = memeName
		self.location = memeLocName
		self.picFormat = memePicFormat
		self.font = 'Roboto-Black.ttf'

	def addSlide(self, name, coordinates, linesize, maxlines):
		self.data[self.counter] = { 	'name' : name,
					'x' : coordinates[0],
					'y' : coordinates[1],
					'linesize' : linesize,
					'maxlines' : maxlines}
		self.counter += 1

	def displayMeme(self):
		display = []
		display.append( "Meme Name:\t" )
		display.append( self.name )
		display.append( "\nNumber of Templates:\t" )
		display.append( str(self.counter) + "\n\n\n" )
		count = 1

		for template in self.data:
			display.append( str(count) )
			count += 1
			display.append( ".\nName:\t" )
			display.append( self.data[template]['name'] )
			display.append( "\nMax. Chars:\t" )
			display.append( str(self.data[template]['linesize'] * self.data[template]['maxlines']) )
			display.append( "\n_________\n\n" )

		return ''.join(display)

	def numberOfTemplates(self):
		return (self.counter + 1)

	def memeControl(self, userText, formatting = None):
		AllLines = []

		for template in range (0, self.counter, 1):
			if (len(userText[template]) >= (self.data[template]['linesize'] * self.data[template]['maxlines'])):
				return ("ERROR: TOO MANY WORDS FOR TEMPLATE#\t"+str(template+1))

			TotalLines = []
			tempWord = []
			count = 0

			if (formatting != None):
				for i in range(0, len(userText[template]), self.data[template]['linesize']):
					TotalLines.append(userText[template][i:i+self.data[template]['linesize']])

				#print (TotalLines)
				break
				#self.printImage(TotalLines, template)
				#return 1

			while (len(userText[template]) != 0):
				tempWord = (userText[template][:self.data[template]['linesize']])

				if (len(tempWord) < self.data[template]['linesize']):
					TotalLines.append(''.join(tempWord))
					userText[template] = ''
					break

				if (tempWord[self.data[template]['linesize']-1] not in punc):
					if (userText[template][self.data[template]['linesize']] in punc):
						TotalLines.append(''.join(tempWord))
						userText[template] = userText[template][self.data[template]['linesize']+1:]

					else:
						enum = 0
						referrer = self.data[template]['linesize']-1

						while (tempWord[referrer-enum] not in punc):
							tempWord = tempWord[:-1]
							enum += 1

						userText[template] = userText[template][referrer-enum+1:]
						TotalLines.append(''.join(tempWord))

				else:
					TotalLines.append(''.join(tempWord))
					userText[template]=userText[template][self.data[template]['linesize']:]

			AllLines.append(TotalLines)

		return AllLines

		def printImage(self, AllLines):
			image = Image.open(self.location+"."+self.picFormat)
			font = ImageFont.truetype(str(self.font), size = 30)
			color = 'rgb(0,0,0)'

			draw = ImageDraw.Draw(image)

			for template in range(0, self.counter, 1):
				count = 0
				for line in AllLines[template]:
					draw.text( (self.data[template]['x'], self.data[template]['y']+(30*count)), str(line), fill=color, font=font)
					count += 1

			image.save("MemeMaker9000/"+self.location+"Modify."+self.picFormat)
			return ("MemeMaker9000/"+self.location+"Modify."+self.picFormat)


class MemeMaker9000:
    def __init__(self, bot):
        self.memeBot = bot

    @memeBot.command(name = "makeMeme",
    brief = "Make-a-Meme using existing templates",
    description = "Welcome to MemeMaker9000!!! v"+version
                    "\nThis bot currently has these templates:"
                    "\n\t>Drake Meme"
                    "\n\t>I'm in Danger Meme"
                    "\n\t>The-guy-looking-at-another-girl-while-his-girl-looks-at-him-in-shock Meme"
                    "\n\t>Gru Meme (Inactive. Do Not Use)"
                    "\n\nSyntax:\n"
                    "\n++makeMeme"
                    "\nENTER TEMPLATE: (Drake- 1) (I'm In Danger- 2) (Disctracted- 3)"
                    "\n2"
                    "\nMeme Name: I'm In Danger"
                    "\nNumber of Templates: 1"
                    "\n1."
                    "\nNormalLines"
                    "\nMax. Chars: 175"
                    "\n_________"
                    "\n\nENTER WORDS FOR TEMPLATE:  1"
                    "\nWhen you see BlueCereal coming to you with a smiley face "
                    "and you know it's going to be something cringy"
                    "\n\nNote:"
                    "\n1. Type exitBlue at any point of the process to exit.",
                    pass_context=True)
    async def makeMeme(ctx):
		allMessages = []
		allMessages.append(ctx.message)

        if "override" in str(ctx.message.content)
            formatting = 1

        drake = memeFormat("Drake Meme", "DrakeMeme", "jpg")
        drake.addSlide("DrakeTop", (350, 20), 15, 6)
        drake.addSlide("DrakeDown", (350, 290), 15, 6)

        imInDanger = memeFormat("Im In Danger Meme", "imInDanger", "png")
        imInDanger.addSlide("NormalLines", (30, 20), 35, 5)

        memeTemplates = [drake, imInDanger]

        entryMsg = await memeBot.send_message(ctx.message.channel, "```Welcome to MemeMaker9000 v"+version+"
        "\nENTER TEMPLATE: (Drake- 1) (I'm In Danger- 2)```")
		allMessages.append(entryMsg)

        memesterChoiceMsg = await memeBot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
		allMessages.append(memesterChoiceMsg)

        try:
            memesterChoice = int(memesterChoiceMsg.content)
        except:
            failedMsg = await memeBot.send_message(ctx.message.channel, "```DATA ENTERED IS NOT AN INTEGER. ABORTED```")
			allMessages.append(failedMsg)
			await memeBot.delete_messages(allMessages)
			return 0

        if (memesterChoice > 3) or (memesterChoice < 1):
            failedMsg = await memeBot.send_message(ctx.message.channel, "```DATA ENTERED IS NOT BETWEEN 1 AND 3. ABORTED```")
			allMessages.append(failedMsg)
			await memeBot.delete_messages(allMessages)
			return 0

        memesterChoice -= 1

        displayData = memeTemplates[memesterChoice].displayMeme()

        displayDataMsg = await memeBot.send_message(ctx.message.channel, "```"+str(displayData)+"```")
		allMessages.append(displayDataMsg)

        memesterLines = []

        for templateNum in range(0, memeTemplates[memesterChoice].numberOfTemplates() - 1, 1):
            templateDefineMsg = await memeBot.send_message(ctx.message.channel, "```ENTER WORDS FOR TEMPLATE:\t", str(templateNum+1))
			allMessages.append(templateDefineMsg)

            memesterLineMsg = await memebot.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
			allMessages.append(memesterLineMsg)

			if (memesterLineMsg.content.lower() == "exitblue"):
                failedMsg = await memeBot.send_message(ctx.message.channel, "```ABORTED```")
				allMessages.append(failedMsg)
				await memeBot.delete_messages(allMessages)
				return 0

            memesterLines.append(memesterLineMsg.content)

        response = memeTemplates[memesterChoice].memeControl(memesterLines)

		if "ERROR: TOO MANY WORDS" in response:
			responseMsgSend = await memeBot.send_message(ctx.message.channel, "```"+str(response)+"```")
			allMessages.append(responseMsgSend)
			failedMsg = await memeBot.send_message(ctx.message.channel, "```ABORTED```")
			allMessages.append(failedMsg)

			await memeBot.delete_messages(allMessages)
			return 0

		MemeLoc = memeTemplates[memesterChoice].printImage(response)

		with open(MemeLoc, 'rb') as meme:
			ImgMsg = await memeBot.send_file(destination=ctx.message.channel, fp=meme, filename=MemeLoc, content=(str(ctx.message.author)+"'s Meme"))

		checkProperMsg = await memeBot.send_message(destination=ctx.message.channel, "```PLEASE CLICK ON 👍 OR 👎 TO RATE THE PERFORMANCE WITHIN THE NEXT 10 SECONDS```")
		allMessages.append(checkProperMsg)

		await memeBot.add_reaction(checkProperMsg, '👍')
		await memeBot.add_reaction(checkProperMsg, '👎')

		reactionReply = await memeBot.wait_for_reaction(emoji=['👎', '👍'], user=ctx.message.author, timeout=10, message=checkProperMsg)

		try:
			if reactionReply[0].emoji == '👍:
				pass
			if reactionReply[0].emoji == '👎':
				#await self.askFeedback(ctx, "MemeMaker9000")
		except:
			pass

		await memeBot.delete_messages(allMessages)

	async def askFeedback(ctx, feedbackFor):
		allMessages = []
		Server = memeBot.get_server(ctx.message.server.id)
		userFeedbackID = Server.get_member(ctx.message.author.id)

		embedTitle = "Feedback For:\t"+str(feedbackFor)
		embedThumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/d/db/Angry_robot.svg/2000px-Angry_robot.svg.png"

		embedDesc = "Ehh.... sorry to hear that something didn't turn out the way you wanted it to."
		embedDesc += "\n\nBut this is reality and get used to it. Quit whining and go back to your normal and primitive"
		embedDesc += " life that you think is so amazing.... Everything goes wrong in your life anyway, so no surprise."
		embedDesc += "\n\nBut you can send some feedback about what happened. You have 150 seconds to give feedback. If you don't want to, just type no."

		feedbackEmbed = discord.Embed(title=embedTitle, description=embedDesc, colour=discord.Colour.dark_purple())

		feedbackMsg = await memeBot.send_message(destination=userFeedbackID, embed=feedbackEmbed)
		allMessages.append(feedbackMsg)

		await memeBot.wait_for_message(timeout = 150, author=ctx.message.author, channel=userFeedbackID, timeout=)

		feedback = feedbackResponseMsg.content

		sendGoodbyeMsg = await memeBot.send_message(userFeedbackID, "```GO ON WITH YOUR LIFE SCUM. THIS MESSAGE WILL SELF DESTRUCT IN 5 SECONDS```")
		allMessages.append(sendGoodbyeMsg)

		await asyncio.sleep(5)
		await memeBot.delete_messages(allMessages)

		if feedback.lower() == "no" or feedback.lower() == "n":
			return 0

		feedbackReport = "FeedBack:\t"+str(feedbackFor)
		feedbackReport += "\nUser:\t"+str(ctx.message.author)
		feedbackReport += "\nServer:\t"+str(ctx.message.server.name)
		feedbackReport += "\n\n"+str(feedback)

		#sendFeedbackReportToMe(feedbackReport)
