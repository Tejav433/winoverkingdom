# Problem 1 : A GOLDEN CROWN
# LANGUAGE  : PYTHON 2.7.6


# GLOBAL DECLARATION OF KINGDOMS AND THEIR EMBLEMS

kingdoms = {'land':'panda','water':'octopus','ice':'mammoth','air':'owl','fire':'dragon','space':'gorilla'}

# METHOD TO PRINT THE RULER AND ALLIES

def printrulerandallies(king,allies):

	print "\n\nWho is the ruler of Southeros?"

	# PRINT THE KING

	print king

	print "Allies of Ruler?"

	# PRINT THE ALLIES

	print allies


# METHOD TO SEND MSG TO KINGDOMS 

def sendmsgtokingdoms():

	print "\n\nInput Messages to kingdoms from King Shan:"

	# TAKING THE INPUT FOR MSG SEND TO NO OF KINGDOMS

	while True:

		print "Enter the no of kingdoms you want to send Messages (Enter only In this range 1 to 5):"

		n = input()

		if(n>5):

			print "Enter correct value there are only 5 kingdoms\n"

		else:

			break


	allie_list = []

	for i in range(0,n):

		# CHECKING THE MSG TO WINOVER THEM OR NOT IF WIN APPEND TO THE ALLIE LIST

		result = checkwinoverthem(raw_input())

		if(result != 0):

			allie_list.append(result.capitalize())
		


	# CHECKING THE  NO OF KINGDOMS WIN IF GREATER THAN OR EQUAL TO 3 THEN KING SHAN WILL BE THE KING ELSE NONE

	
	if(len(allie_list) >= 3):

		king = "King Shan"

		allies = ",".join(allie_list)

	else:

		king = "NONE"

		allies = "NONE"

	printrulerandallies(king,allies)


# METHOD TO CHECK WIN OVER THEM THROUGH MSG

def checkwinoverthem(x):

	# SPLIT THE INPUT MSG TO SEPARATE KINGDOM AND ACTUAL MSG

	msg_split = x.split(',')

	kingdom = msg_split[0].lower()

	message = msg_split[1].lower()

	# TAKING DISTINCT CHARACTERS FROM KINGDOM EMBLEM

	kingdom_emb_distnict = set(kingdoms[kingdom])

	flag = 0

	# COMPARING THE COUNT OF EMBLEM CHARACTERS IN THE MSG TO CHECK ALL ARE PRESENT IN THE MSG

	for i in kingdom_emb_distnict:

		if(kingdoms[kingdom].count(i) > message.count(i)):

			flag = 1

			break

	if(flag == 0):

		return kingdom

	else:

		return 0


# main function call

printrulerandallies('NONE','NONE')

sendmsgtokingdoms()









