from check_WinOverKingdom import CheckWinOverKingdom
from print_RulerandAllies import PrintRulerandAllies


class GoldenCrown:

	none = "NONE"

	def __init__(self,king_name,rule_kingdom,min_kgdms):

		self.min_kingdoms_for_ruler = min_kgdms
		self.king_name = king_name
		self.rule_kingdom = rule_kingdom

	# method to take the input for no of kingdoms to send messages for allegiance
	def inputForNoofKingdoms(self):

		while True:
			print "Enter the no of kingdoms you want to send Messages (Greater than or Equal to 3):"
			n = input()
			if(n < self.min_kingdoms_for_ruler):
				print "Enter correct value (Greater than or Equal to 3) \n"
			else:
				break
		return n

	# method to take input messages to send kingdoms and check for their allegiance[greater than or eqaul to 3]
	def inputMsgtoKingdoms(self):

		print "\n\nInput Messages to kingdoms from King Shan:"
		n = self.inputForNoofKingdoms()
		allie_list = []

		for i in range(0,n):
			result = CheckWinOverKingdom().checkWinOverP1(raw_input())
			if(result != 0 and result != self.rule_kingdom):
				allie_list.append(result.capitalize())

		allie_list = list(set(allie_list))

		if(len(allie_list) >=self. min_kingdoms_for_ruler):
			king = self.king_name
			allies = ",".join(allie_list)
		else:
			king = self.none
			allies = self.none

		PrintRulerandAllies(king,allies)

# printing the ruler and allies
PrintRulerandAllies('NONE','NONE')
# object creation & call the method
obj = GoldenCrown("King Shan","space",3)
obj.inputMsgtoKingdoms()

	


