
def ccProvider(operations):
	
	balance_info = {} 

	for ops in operations:
		if ops[0] == "Add":
			# "Add", "Tom", "4111111111111111", "$1000"
			# if validate cc num passes:
			limit = int(ops[3].split('$')[1])
			
			if luhn_check(ops[2]) == True:	
				balance_info[ops[1]] = {'card_number': ops[2], 'limit': limit, 'balance': 0}

			else:
				balances_info[ops[1]]= {'card_number': 'invalid', 'limit': limit, 'balance': 'error'}


		elif ops[0] == "Charge":
			charge = int(ops[2].split('$')[1])
			if balance_info[ops[1]]['balance'] + charge > balance_info[ops[1]]['limit']:
				pass

			else:
				balance_info[ops[1]]['balance'] += charge


		elif ops[0] == "Credit":
			credit = int(ops[2].split('$')[1])
			balance_info[ops[1]]['balance'] -= credit

	
	balance_output = []

	for person in balance_info:
		balance = balance_info[person].get('balance')
		balance_output.append[person, balance]
		# print(person)
		# print(balance_info[person].get('balance'))

	# 	balance_output.append[person, person['balance']]

	# print(balance_output)



# card_number --> validate w. luhn 0



# "charge"
# against luhn 10 invalid cards are ignored. ??

# "credit"
# credits against luhn 10 cards are ignores


# return card holder names with balance associated.
# display "error" instead of balance if cc does not
# pass Luhn10. Display in lexicographical(alpha) order

# operations = [["Add", "Tom", "4111111111111111", "$1000"],
#               ["Add", "Lisa", "5454545454545454", "$3000"],
#               ["Add", "Quincy", "1234567890123456", "$2000"],
#               ["Charge", "Tom", "$500"],
#               ["Charge", "Tom", "$800"],
#               ["Charge", "Lisa", "$7"],
#               ["Credit", "Lisa", "$100"],
#               ["Credit", "Quincy", "$200"]]

# creditCardProvider(operations) = [["Lisa", "$-93"],
#                                   ["Quincy", "error"],
#                                   ["Tom", "$500"]]

ccProvider([["Add", "Tom", "4111111111111111", "$1000"],
              ["Add", "Lisa", "5454545454545454", "$3000"],
              ["Add", "Quincy", "1234567890123456", "$2000"],
              ["Charge", "Tom", "$500"],
              ["Charge", "Tom", "$800"],
              ["Charge", "Lisa", "$7"],
              ["Credit", "Lisa", "$100"],
              ["Credit", "Quincy", "$200"]])