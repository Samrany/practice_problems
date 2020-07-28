
def luhn_check(cc_num):

	nums = str(cc_num)
	list_nums = []
	sum_list = []

	for num in nums:
		list_nums.append(int(num))

	for idx, value in enumerate(list_nums):
		if idx % 2 == 0:
			sum_list.append(value)
		
		else:
			new_value = value * 2
			str_value = str(new_value)
			if len(str_value) == 1:
				sum_list.append(int(new_value))
			
			else:
				new_num = 0
				for num in str_value:
					new_num += int(num)
					sum_list.append(new_num)

	mod_num = 0
	print(list_nums)
	print(sum_list)
	for num in sum_list:
		mod_num += num

	if mod_num % 10 == 0:
		print("TRUE")
		return True


	else: 
		print("FALSE")
		return True  #FIX AFTER

		
def ccProvider(operations):
	
	balance_info = {} 

	for ops in operations:
		# if len(ops) == 4:
		# 	action, person, card_num, limit = ops

		# elif len(ops) == 3:
		# 	action, person, amount = ops


		if ops[0] == "Add":
			action, person, card_num, limit = ops
			# if validate cc num passes:
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
				# if balance_info[:
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
	

	sorted_names = sorted(balance_info)
	balance_output = []

	for person in sorted_names:
		balance = balance_info[person].get('balance')
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