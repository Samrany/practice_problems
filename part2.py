
def luhn_check(cc_num):

	nums = str(cc_num)
	list_nums = []
	sum_list = []

	for num in nums:
		list_nums.append(int(num))

	count = 0
	for item in list_nums[-1::-1]:
		count += 1

		if count % 2 != 0:
			sum_list.append(item)

		else:			
			value = item * 2
			
			if len(str(value)) == 1:
				sum_list.append(value)

			else: 
				str_value = str(value)
				added_nums = int(str_value[0]) + int(str_value[1])
				sum_list.append(added_nums)


	if sum(sum_list) % 10 == 0:
		return True

	else:
		return False

		
def ccProvider(operations):
	
	balance_info = {} 

	for ops in operations:
		# if len(ops) == 4:
		# 	action, person, card_num, limit = ops

		# elif len(ops) == 3:
		# 	action, person, amount = ops


		if ops[0] == "Add":
			action, person, card_num, limit = ops
			limit = int(limit.split('$')[1])
			
			if luhn_check(card_num) == True:	
				balance_info[person] = {'card_number': card_num, 'limit': limit, 'balance': 0}

			else:
				balance_info[ops[1]]= {'card_number': card_num, 'limit': limit, 'balance': 'error'}

		# could do "else unpack this way --> check if balance == error, pass if not continue to determine
		#if action = charge or credit

		elif ops[0] == "Charge":
			action, person, amount = ops
			charge = int(amount.split('$')[1])
			
			if balance_info[person]['balance'] == 'error' or (
				balance_info[person]['balance'] + charge > balance_info[person]['limit']): 
				pass

			else:
				balance_info[person]['balance'] += charge


		elif ops[0] == "Credit":
			action, person, amount = ops
			credit = int(amount.split('$')[1])
			
			if balance_info[person]['balance'] == 'error':
				pass
			
			else:
				balance_info[person]['balance'] -= credit
	
		else:
			#runtime error

	sorted_names = sorted(balance_info)
	balance_output = []
	#SORTED DICTIONARY ITEMS. PYTHON 3.6 DICTIONARIES ARE ORDERED?

	for person in sorted_names:
		balance = (balance_info[person].get('balance'))

		if balance == "error":
			pass
			
		else:
			balance = '$'+str(balance)
		
		balance_output.append([person, balance])

	print(balance_output)
	return(balance_output)




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

# ccProvider(operations) = [["Lisa", "$-93"],
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