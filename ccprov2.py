
def luhn_check(cc_num):
	""""""

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



def cc_add(operation):
	""""""
	action, person, card_num, limit = operation
	limit = int(limit.split('$')[1])
	
	add_dict = {}

	if luhn_check(card_num) == True:	
		add_dict[person] = {'card_number': card_num, 'limit': limit, 'balance': 0}

	else:
		add_dict[person]= {'card_number': card_num, 'limit': limit, 'balance': 'error'}

	return add_dict


def cc_charge(operation):
	""""""
	charge_dict = {}
	action, person, charge = operation
	charge = int(amount.split('$')[1])
	
	if charge_dict[person]['balance'] == 'error' or (
		charge_dict[person]['balance'] + charge > balance_info[person]['limit']): 
		pass

	else:
		balance_info[person]['balance'] += charge




def ccProvider(operations):
	""""""
	
	balance_info = {} 

	for op in operations:

		if op[0] == "Add":
			balance_info.update(cc_add(op))


		elif op[0] == "Charge":
			balance_info.update(cc_charge(op))


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
		balance = (balance_info[person].get('balance'))

		if balance == "error":
			pass
			
		else:
			balance = '$'+str(balance)
		
		balance_output.append([person, balance])

	print(balance_output)
	return(balance_output)





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