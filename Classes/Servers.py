from datetime import datetime
from ast import literal_eval as parseData
import os
from subprocess import run

"""
Documentation:
Write MemberData as:
memberID,
botCalls,
warnings[],
strikes[],

Write ServerData as:
serverID,
serverName,
botcalls

"""
def getMemberData(memberID, serverID):
	try:
		FileObj = open(str(serverID)+"/"+str(memberID), 'r')
		data = FileObj.read()
		FileObj.close()
		parsedData = parseData(data)
		return Data
	except:
		return (-1)

#TO WRITE FOR STRIKES OR WARNINGS
def writeMemberData(memberID, serverID, warning = None, strike = None):
	#Check if the file exists:
	data = getMemberData(memberID, serverID)
	#FirstLogEntry
	if (data == (-1)):
		warningList = []
		strikeList = []

		if (warning != None):
			warningList.append(warning)

		if (strike != None):
			strikeList.append(strike)

		newMemberDict = {"memberID" : memberID,
						"botCalls" : {},
						"warnings" : warningList,
						"strikes" : strikeList}
		FileObjNew = open(str(serverID)+"/"+str(memberID), 'w')
		FileObjNew.write(str(newMemberDict))
		FileObj.close()
		return 1
	else:
		warnings = data["warnings"]
		strikes = data["strikes"]
		if (warning != None):
			data["warnings"].append(warning)
			if ( (len(warning) == 3) or (len(warning) == 6) or (len(warning) == 9) ):
			#	addStrike(memberID, serverID, adminID = "SuperUserBot", reasonNumber = )

#WHEN A USER USES A BOT CALL
def addBotCall(memberID, serverID, callName):
	try:
		FileObj = open(str(serverID)+"/"+str(memberID), 'r')
		data = FileObj.read()
		memberData = parseData(data)

		try:
			memberData["botCalls"][callName] += 1
		except:
			memberData["botCalls"][callName] = 1

		FileObj.close()
		os.remove(str(serverID)+"/"+str(memberID))
		FileObjNew = open(str(serverID)+"/"+str(memberID), 'w')
		FileObjNew.write(str(memberData))
		FileObjNew.close()
	except:
		FileObjNewMember = open(str(serverID)"/"+str(memberID), 'w')

		warningList = []
		strikeList = []

		newMemberDict = {"memberID" : memberID,
						"botCalls" : {},
						"warnings" : warningList,
						"strikes" : strikeList}

		newMemberDict["botCalls"][callName] = 1

		FileObjNewMember.write(str(newMemberDict))

def setPollChannel(serverID, pollChannelID):
	try:
		FileObj = open(str(serverID)+"/"+"MainData", 'r')
		data = parseData(FileObj.read())
		data["pollChannelID"] = pollChannelID
		FileObj.close()
		os.remove(str(serverID)+"/MainData")
		FileObjNew = open(str(serverID)+"/MainData", 'w')
		FileObjNew.write(str(data))
	except:
		FileObj = open(str(serverID)+"/MainData", 'w')
		data = {}
		data["pollChannelID"] = pollChannelID
		FileObj.close()

	return 0

def getPollChannel(serverID):
	try:
		FileObj = open(str(serverID)+"/MainData", 'r')
		data = parseData(FileObj.read())
		try:
			pollChannelID = data["pollChannelID"]
			return pollChannelID
		except:
			return 0
	except:
		return -1

def setAdminBotControlChannel(serverID):
	run(['mkdir', str(serverID)])
	FileObj = open(str(serverID)+"/MainData", 'w')
	data = {}
	data["adminBotControlChannel"] = str(serverID)
	FileObj.write(str(data))
	FileObj.close()
	return 1
