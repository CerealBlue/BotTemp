from datetime import datetime
from ast import literal_eval as parseData


"""
Documentation:

Class serversData contains:
	servers:
		"name": "Name"
		"calls": CallsFromThatServer
		"members":
			memberID:
				"messages": totalMessages
				"warnings":
					date: [adminID, reasonNumber]
				"strikes":
					date: [adminID, reasonNumber]
				"botCalls":
					botcallName: NumberOfTimesItWasCalled
					
"""

class serversData:
	def __init__(self):
 		self.servers = {}

	def addServer(self, ID, Name):
		self.servers[ID] = {}
		self.servers[ID]["name"] = Name
		self.servers[ID]["calls"] = 0
		self.servers[ID]["members"] = {}

	def addMemberToServer(self, serverID, memberID):
		self.servers[serverID]["members"][memberID] = {}
		self.servers[serverID]["members"][memberID]["messages"] = 0
		self.servers[serverID]["members"][memberID]["warnings"] = {}
		self.servers[serverID]["members"][memberID]["strikes"] = {} 
		self.servers[serverID]["members"][memberID]["botCalls"] = {}

	def message(self, serverID, memberID):
		self.servers[serverID]["members"][memberID]["messages"] += 1
		self.writeDataToFile(self, serverID)

	def addBotCall(self, serverID, memberID, botCall):
		self.servers[serverID]["calls"] += 1

		try:
			self.servers[serverID]["members"][memberID]["botCalls"][botCall]  += 1
		except:
			self.servers[serverID]["members"][memberID]["botCalls"][botCall]  = 1
	

	def writeDataToFile(self, serverID):
		os.remove(self.servers[serverID]["name"]+"_Data_SUBOT")
		FileObj = open(self.servers[serverID]["name"]+"_Data_SUBOT", 'w')
		FileObj.write(str(self.servers[serverID]["members"]))
	
	def updateServer(self, serverID, directory = None):
		FileObj = open(directory+self.servers[serverId][]+"_Calls_Data", 'r')
		data = FileObj.read()
		FileObj.close()
		parsedData = parseData(data)
		self.servers[serverID]["members"] = {}
		self.servers[serverID]["members"] = parsedData
		return parsedData

	def numberOfCalls(self, serverID):
		return self.servers[serverID]["calls"]

	def getServersNames(self):
		servers = []
		for server in self.servers:
			servers.append(self.servers[server]["name"])

		return servers

	def getServersID(self):
		servers = []
		for server in self.servers:
			servers.append(server)
		return 

	def getServerID(self, serverName):
		for server in self.servers:
			if (serverName == self.servers[server]["name"]):
				return server

	def addWarning(self, serverID, adminMemberID, warnedMemberID, reasonNumber):
		
		self.servers[serverID]["members"][warnedMemberID]["warnings"][str(datetime.datetime.now().date())] = [adminMemberID, reasonNumber]
		count = len(self.servers[serverID]["members"][warnedMemberID]["warnings"])

		if (count == 3) or (count == 6) or (count == 9):
			self.addStrikeBlue(serverID, "BlueCereal", warnedMemberID, 0)
		
	def addStrike(self, serverID, adminMemberID, strikedMemberID, reasonNumber):
		self.servers[serverID]["members"][warnedMemberID]["strikes"][str(datetime.datetime.now().date())] = [adminMemberID, reasonNumber]
		count = len(self.servers[serverID]["members"][strikedMemberID]["strikes"])

		if (count >= 3):
			#alertMe(ReasonNumber, strikedMemberID, serverID)

	def returnMisbehavior(self, serverID, memberToCheckID):
		return (self.servers[serverID]["members"][memberToCheckID]["warnings"], self.servers[serverID]["members"][memberToCheckID]["strikes"])

	def clearMisbehaviour(self, serverID, callerID, serverIDTarget, memberToClearID, clearList):
		adminFile = open("BlueCereal", 'r')
		myID = adminFile.readline()
		myServerID = adminFile.readline()
		adminFile.close()

		if (serverID == myServerID):
			if (callerID == myID):
				for listItem in clearList:
					self.servers[serverIDTarget]["members"][memberToClearID][listItem] = []
				return 1
		#alertMe(ReasonNumber)
		return (-1)

"""self.me = '378555841017544724'"""
	"""def myId(self):
		return self.me

	def isMe(self, testId):
		if (self.me == testId):
			return True
		return False"""	
