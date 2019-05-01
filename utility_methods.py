from kingdom_list import KingdomList
import random

class UtilityMethods:

	msgs_filename = "messages.txt"

	def __init__(self):

		self.kingdoms = KingdomList.kingdoms

	# method to get random msg from given messages txt
	def get_random_msg(self):

		lines = open(self.msgs_filename).read().splitlines()
		message =random.choice(lines)
		return message

	# method to convert the strings in a list to  lowercase 
	def convert_lower(self,msg_list):

		for i in range(0,len(msg_list)):
			msg_list[i] = msg_list[i].lower()
		return msg_list

	# method to get the non compete kingdoms list for Ruler
	def get_non_compete_kingdoms(self,compete_kingdoms):

		non_compete_kingdoms = []
		kingdom = self.kingdoms.keys()
		for i in kingdom:
			if i not in compete_kingdoms:
				non_compete_kingdoms.append(i)
		return non_compete_kingdoms

	# method to get six random msg from ballet box
	def get_six_random_msg(self,ballot_list):

		random.shuffle(ballot_list)
		six_random_msg = ballot_list[:6]
		return six_random_msg

	# method to declare and intialize the dictionary object for given key&values
	def get_dict_object(self,intialize,compete_kingdoms):

		dict_object = {}
		for i in compete_kingdoms:
			dict_object[i] = intialize
		
		return dict_object
	# method to print the given list
	def printmsg(self,li):
		print "Message that are picked randomly by High priest :\n"
		for i in li:
			print "\n",i
		print "\n"





