# PROBLEM 2 :  BREAkER OF CHAINS
# LANGUAGE  : PYTHON 2.7.6


import random

# GLOBAL DECLARATION OF KINGDOMS AND THEIR EMBLEMS
kingdoms = {'land':'panda','water':'octopus','ice':'mammoth','air':'owl','fire':'dragon','space':'gorilla'}

# METHOD TO PRINT THE RULER AND ALLIES
def printrulerandallies(king,allies):

	print "\n\nWho is the ruler of Southeros?"

	# PRINT THE KING
	print king

	print "Allies of Ruler?"

	# PRINT THE ALLIES
	print allies,"\n"

# METHOD TO SELECT RANDOM MESSAGE FROM THE GIVEN TXT FILE
def get_random_msg():

	lines = open('messages.txt').read().splitlines()

	myline =random.choice(lines)

	return myline

# CONVERTING TO LOWERCASE 
def convert_lower(x):

	for i in range(0,len(x)):

		x[i] = x[i].lower()

	return x

# METHOD TO GET THE NON COMPETE KINGDOMS
def get_non_compete_kingdoms(kingdoms,compete_kingdoms):

	non_compete_kingdoms = []

	kingdom = kingdoms.keys()

	for i in kingdom:

		if i not in compete_kingdoms:

			non_compete_kingdoms.append(i)

	return non_compete_kingdoms

# METHOD TO CHECK WIN OVER THEM THROUGH MSG
def checkwinoverthem(receive_kingdom,message):

	# TAKING DISTINCT CHARACTERS FROM KINGDOM EMBLEM
	kingdom_emb_distnict = set(kingdoms[receive_kingdom])

	flag = 0

	# COMPARING THE COUNT OF EMBLEM CHARACTERS IN THE MSG TO CHECK ALL ARE PRESENT IN THE MSG
	for i in kingdom_emb_distnict:

		if(kingdoms[receive_kingdom].count(i) > message.count(i)):

			flag = 1

			break

	if(flag == 0):

		return 1
	else:

		return 0

def ballot_system(compete_kingdoms,rounds):

	# DECLARATION OF A LIST TO STORE BALLOT BOX MESSAGES
	ballot_list = []

	# APPEND THE MESSAGES THAT ARE COMPETE KINGDOMS SENDING TO OTHER KINGDOMS FOR ALLEGIANCE
	for i in range(0,len(compete_kingdoms)):

		for key in kingdoms.keys():

			if(key != compete_kingdoms[i] and key not in compete_kingdoms):

				# MESSAGE FORMAT SENDER KINGDOM,RECEIVE KINGDOM ,RANDOM MESSAGE FROM GIVEN TXT FILE
				ballot_list.append(compete_kingdoms[i]+','+key+','+get_random_msg())

	# SHUFFLING THE MESSAGES IN BALLOT BOX
	random.shuffle(ballot_list)

	#PICKING SIX RANDOM MESSAGES BY HIGH PRIEST
	six_random_msg = ballot_list[:6]

	# TO GET THE NOT COMPETE KINGDOMS FOR ALLEGIANCE
	non_compete_kingdoms = get_non_compete_kingdoms(kingdoms,compete_kingdoms)

	#DECLARING A DICTIONARY FOR STORING COMPETE KINGDOMS RESULTS
	final_result_allies_count = {}
	final_result_allies = {}

	for i in compete_kingdoms:

		final_result_allies_count[i] = 0
		final_result_allies[i] = ''

	# TAKING THE NON COMPETE KINGDOMS AND THEIR ALLEGIANCE FOR THE RESULT
	for i in non_compete_kingdoms:

		# ITERATE THE HIGH PRIEST TAKEN MESSAGES AND COMPARE AND CHECK FOR THE ALLEGIANCE
		for j in six_random_msg:

			# MESSAGE SPLITTING TO GET THE SENDER KINGDOM ,RECEIVE KINGDOM ,MESSAGE
			msg_split = j.split(',')

			sender_kingdom = msg_split[0].lower()

			receive_kingdom = msg_split[1].lower()

			message = msg_split[2].lower()

			# IF THE RECEIVE KINGDOM AND NON COMPETE KINGDOM EQAUL THEN CHECKING WIN OVER THEM OR NOT
			if(i == receive_kingdom):

				result = checkwinoverthem(receive_kingdom,message)

				# IF RESULT 1 THEN SENDER KINGDOM WIN OVER THE RECEIVE KINGDOM SO THE ALLIES COUNT INCREMENTED
				if(result == 1):

					final_result_allies_count[sender_kingdom] = final_result_allies_count[sender_kingdom]+1
					final_result_allies[sender_kingdom] = final_result_allies[sender_kingdom]+i.capitalize()
	
	#PRINTING THE COMPETE KINGDOMS AND THEIR ALLIES COUNT
	print "Results After round ",rounds," ballot count :"

	for i in final_result_allies_count.keys():

		print "Allies for ",i.capitalize()," :",final_result_allies_count[i]

	# TAKING THE MAXIMUM VALUE FROM THE RESULT
	val = final_result_allies_count.values()

	max_val = max(val)

	# CHECKING IF THERE ANY TIE BETWEEN KINGDOMS IF TIE THEN TAKING TIE KINGDOMS ELSE TAKING THE MAX ALLIES COUNT KINGDOM
	lis = [k for k,v in final_result_allies_count.items() if v == max_val]

	# IF THERE IS NO TIE PRINTING THE RULER AND ALLIES ELSE REPEAT THE BALLOT SYSTEM PROCESS FOR TIED KINGDOMS
	if(len(lis) == 1):
		printrulerandallies(lis[0].capitalize(),final_result_allies[lis[0]])
	else:
		ballot_system(lis,rounds+1)



# MAIN FUNCTION CALL
printrulerandallies('NONE','NONE')

compete_kingdoms = convert_lower(raw_input().split())

ballot_system(compete_kingdoms,1)




