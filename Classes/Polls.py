import discord
from discord.ext import commands

class polls:
    def __init__(self, bot):
        self.botPolls = bot

    @botPolls.command(name="MakePoll",
                        description="This command makes the bot create a poll for you"
                        "\n\nNotes:"
                        "\n1. You must be an Admin to use this feature."
                        "\n2. You must have defined a poll channel using ++setPollChannel. This is the target channel"
                        "\n3. If you choose poll type-2 (a poll with options), you can set 9 options (max)."
                        "\n3. To cancel the poll at any instant, type exitBlue"
                        "\nThere are two types of polls."
                        "\n1. Yes or No"
                        "\n2. Options"
                        "\n\nSyntax (for Y/N):"
                        "\n++MakePoll"
                        "\nTYPE (1/2) FOR (\"Y/N\" OR \"OPTIONS\"):"
                        "\n1"
                        "\nENTER THE POLL QUESTION:"
                        "\nDo you think BlueCereal tastes like Cereal?"
                        "\n\nSyntax (for Options):"
                        "\n++MakePoll"
                        "\nTYPE (1/2) FOR (\"Y/N\" OR \"OPTIONS\"):"
                        "\n2"
                        "\nENTER THE POLL QUESTION:"
                        "\nWhat do you think BlueCereal tastes like?"
                        "\nOPTIONS (IF DONE, TYPE completedPoll):"
                        "\nCereal-like"
                        "\nOld and Smelly Cheese"
                        "\nRetarded and Poop-like"
                        "\ncompletedPoll",
                        brief="Make A Poll",
                        pass_context=True,
                        hidden=True)
    async def MakePoll(ctx):
        if ctx.message.author.server_permissions.kick_member:
    		await botAdmin.send_message(ctx.message.channel, "Did you really think I'd let you do that? You're not high enough in the server to use this. 😑")
    		return(0)

        channelTarget = getPollChannel(ctx.message.server.id)

        if channelTarget == 0:
            await botPolls.send_message(ctx.message.channel, "```POLL CHANNEL NOT INITIALIZED. USE ?help setPollChannel```")
            return 0

        if channelTarget == -1:
            await botPolls.send_message(ctx.message.channel, "```BOT NOT INITIALIZED. USE ?help authBot```")
            return 0

        await botPolls.send_message(ctx.message.channel, "```TYPE (1/2) FOR (\"Y/N\" OR \"OPTIONS\")```")
        typePollsMsg = await botPolls.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

        try:
            typePoll = int(typePollMsg.content)
        except:
            await botPolls.send_message(ctx.message.channel, "```ABORTED```")
            return (0)

        if (typePoll != 1) and (typePoll != 2):
            await botPolls.send_message(ctx.message.channel, "```ENTER EITHER 1 OR 2. ABORTED```")
            return (0)

        pollQuestion = []

        if (typePoll == 1):
            await botPolls.send_message(ctx.message.channel, "```ENTER THE POLL QUESTION:```")
            pollQuestionMsg = await botPolls.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            pollQuestion.append(pollQuestionMsg.content)

            if (pollQuestionMsg.content.lower() == "exitblue"):
                await botPolls.send_message(ctx.message.channel, "```ABORTED```")
                return (0)

        if (typePoll == 2):
            await botPolls.send_message(ctx.message.channel, "```ENTER THE POLL QUESTION:```")
            pollQuestionMsg = await botPolls.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)
            pollQuestionappend(pollQuestionMsg.content)
            Options = []

            if (pollQuestionMsg.content.lower() == "exitblue"):
                await botPolls.send_message(ctx.message.channe, "```ABORTED```")
                return (0)

            await botPolls.send_message(ctx.message.channel, "OPTIONS (IF DONE, TYPE completedPoll):")

            optionsMsg = await botPolls.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

            if (optionsMsg.content.lower() == "exitblue"):
                await botPolls.send_message(ctx.message.channel, "```ABORTED```")
                return (0)

            count = 1
            while (optionsMsg.content.lower() != "completedpoll"):
                if (count > 9):
                    break
                Options.append(optionsMsg.content)

                optionsMsg = await botPolls.wait_for_message(author=ctx.message.author, channel=ctx.message.channel)

                if (optionsMsg.content.lower() == "exitblue"):
                    await botPolls.send_message(ctx.message.channel, "```ABORTED```")
                    return (0)

                count += 1

            await botPolls.send_message(ctx.message.channel, "```COMPLETED```")

            #Create Embed
            pollEmbedTitle = str(ctx.message.author)+"'s Poll"
            pollEmbedColour = discord.Colour.blue()
            pollEmbedQuestion = ''.join(pollQuestion)
            pollEmbedThumbnail = "https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Question_mark_white-transparent.svg/2000px-Question_mark_white-transparent.svg.png"

            sendPollEmbed = discord.embed(title=pollEmbedTitle, description=pollEmbedQuestion, colour=pollEmbedColour)
            sendPollEmbed.set_thumbnail(url=pollEmbedThumbnail)

            #START POLL CREATIONS
            if (typePoll == 1):
                """#👎👍#"""

                sendPollEmbed.add_field(name = "To agree, react with", value = "👍")
                sendPollEmbed.add_field(name = "To disagree, react with", value = "👎")

                addReactToMsg = await botPolls.send_message(destination=channelTarget, embed=pollEmbedQuestion)

                await botPolls.add_reaction(addReactToMsg, '👍')
                await botPolls.add_reaction(addReactToMsg, '👎')

            if (typePoll == 2):
                """1\u20e3 to 9\u20e3"""
                unicodeNum = "\u20e3"

                for i in range(0, len(Options), 1):
                    sendPollEmbed.add_field(name = str(i+1)+unicodeNum, value=Options[i])

                addReactToMsg = await botPolls.send_message(destination=channelTarget, embed=pollEmbedQuestion)

                for i in range(0, len(Options), 1):
                    await addReactToMsg.add_reaction(addReactToMsg.id, str(i+1)+unicodeNum)
