from utility_methods import UtilityMethods as U
from kingdom_list import KingdomList
from check_WinOverKingdom import CheckWinOverKingdom
from print_RulerandAllies import PrintRulerandAllies 

class BallotSystem:

	def __init__(self):

		self.kingdoms = KingdomList.kingdoms

	# method to store the compete kingdoms sending messages to another kingdoms for their allegiance 
	# message format sender_kingdom,receive_kingdom,random_msg from given messages txt file
	def ballotbox_list(self,compete_kingdoms):

		ballot_list = []
		for i in range(0,len(compete_kingdoms)):
			for key in self.kingdoms.keys():
				if(key != compete_kingdoms[i] and key not in compete_kingdoms):
					ballot_list.append(compete_kingdoms[i]+','+key+','+U().get_random_msg())
		return ballot_list

	# to select random six messages from the ballet and check the allegiance for ruler kingdom
	def main_logic(self,compete_kingdoms,round_no):

		ruler_allies_count = ruler_allies = {}
		ruler_allies_count = U().get_dict_object(0,compete_kingdoms)
		ruler_allies = U().get_dict_object('',compete_kingdoms)
		non_compete_kingdoms = U().get_non_compete_kingdoms(compete_kingdoms)
		six_random_msg = U().get_six_random_msg(self.ballotbox_list(compete_kingdoms))
		U().printmsg(six_random_msg)

		for i in non_compete_kingdoms:
			for j in six_random_msg:
				msg_split = j.split(',')
				sender_kingdom = msg_split[0].lower()
				receive_kingdom = msg_split[1].lower()
				message = msg_split[2].lower()
				if(i == receive_kingdom):
					result =CheckWinOverKingdom().checkWinOverP2(receive_kingdom,message)
					if(result != 0):
						ruler_allies_count[sender_kingdom] = ruler_allies_count[sender_kingdom]+1
						ruler_allies[sender_kingdom] = ruler_allies[sender_kingdom]+i.capitalize()

		self.print_ballet_results(ruler_allies_count,ruler_allies,round_no)

	# printing the ballet results kingdom wise and print the ruler and allies
	def print_ballet_results(self,ruler_allies_count,ruler_allies,round_no):

		print "Results After round ",round_no," ballot count :"
		for i in ruler_allies_count.keys():
			print "Allies for ",i.capitalize()," :",ruler_allies_count[i]
		res_list = self.get_ruler_or_tie_kingdoms(ruler_allies_count)
		if(len(res_list) == 1):
			PrintRulerandAllies(res_list[0],ruler_allies[res_list[0]])
		else:
			self.main_logic(res_list,round_no+1)

	# to get the ruler kingdom or tie kingdoms
	def get_ruler_or_tie_kingdoms(self,ruler_allies_count):

		val = ruler_allies_count.values()
		max_val = max(val)
		lis = [k for k,v in ruler_allies_count.items() if v == max_val]
		return lis

# object creation for ballotsystem
obj = BallotSystem()
PrintRulerandAllies('NONE','NONE')
print "\nEnter the compete kingoms space separated :\n"
inp = raw_input().split()
obj.main_logic(U().convert_lower(inp),1)		



	

