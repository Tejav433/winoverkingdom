from kingdom_list import KingdomList

class CheckWinOverKingdom:

	def __init__(self):

		self.kingdoms = KingdomList.kingdoms

	# to check allegiance given or not for problem one GOlDEN CROWN
	def checkWinOverP1(self,msg):

		msg_split = msg.split(',')
		receive_kingdom = msg_split[0].lower()
		message = msg_split[1].lower()
		return self.checkWinOverP2(receive_kingdom,message)

	# to check allegiance given or not for problem two BREAKER OF CHAINS
	def checkWinOverP2(self,receive_kingdom,message):

		kingdom_emb_distnict = set(self.kingdoms[receive_kingdom])
		flag = 0
		for i in kingdom_emb_distnict:
			if(self.kingdoms[receive_kingdom].count(i) > message.count(i)):
				flag = 1
				break
		if(flag == 0):
			return receive_kingdom
		else:
			return 0


