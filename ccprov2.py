def ccProvider(operations):
    """Given a list of credit card operations, returns a list of people with their respective balances"""

    balance_info = {}

    for op in operations:

        if op[0] == "Add":
            balance_info.update(cc_add(op))

        elif op[0] == "Charge":
            balance_info.update(cc_charge(balance_info, op))

        elif op[0] == "Credit":
            balance_info.update(cc_credit(balance_info, op))
        
        else:


    return(cc_balances(balance_info))


def cc_add(operation):
    """Given a list of cc info, checks if card passes luhn function and returns dictionary
     with people (key) and respective card_num, limit, and balance of 0, or error if failed luhn test (values)"""

    action, person, card_num, limit = operation
    limit = int(limit.split('$')[1])

    add_dict = {}

    if luhn_check(card_num) == True:
        add_dict[person] = {'card_number': card_num, 'limit': limit, 'balance': 0}

    else:
        add_dict[person]= {'card_number': card_num, 'limit': limit, 'balance': 'error'}

    return add_dict



def cc_charge(balance_info, operation):
    """Given a dictionary of people's cc balance info and a list with cc charge info,
    applies charge to balance if balance doesn't have an error, or if charge will
    not put user over cc limit and returns updated dictionary"""

    action, person, charge = operation
    charge = int(charge.split('$')[1])

    if balance_info[person]['balance'] == 'error' or (
       balance_info[person]['balance'] + charge > balance_info[person]['limit']):
        pass

    else:
        balance_info[person]['balance'] += charge


    return balance_info


def cc_credit(balance_info, operation):
    """Given a dictionary of people's cc balance info and a list with cc credit info,
    applies credit to balance if balance doesn't have an error and returns updated dictionary"""

    _, person, credit = operation
    credit = int(credit.split('$')[1])

    if balance_info[person]['balance'] == 'error':
        pass

    else:
        balance_info[person]['balance'] -= credit

    return balance_info


def cc_balances(balance_info):
    """Given a dictionary of people and their cc info and balances, returns a list sorted alphabetically
    by name	of persons and their balances"""

    sorted_names = sorted(balance_info)
    balance_output = []

    for person in sorted_names:
        balance = (balance_info[person].get('balance'))

        if balance == "error":
            pass

        else:
            balance = '$'+str(balance)

        balance_output.append([person, balance])

    return balance_output


def luhn_check(cc_num):
    """Takes string of cc numbers and determines if credit card number sequence passes the
    luhn test (i.e. if cc is valid) and returns True or False """

    list_nums = []
    sum_list = []

    for num in cc_num:
        list_nums.append(int(num))


    count = 0
    for item in list_nums[-1::-1]:
        count += 1

        if count % 2 != 0:
            sum_list.append(item)

        else:
            value = item * 2

            if value < 10:
                sum_list.append(value)

            else:
                str_value = str(value)
                added_nums = int(str_value[0]) + int(str_value[1])
                sum_list.append(added_nums)


    if sum(sum_list) % 10 == 0:
        return True

    else:
        return False






print(ccProvider([["Add", "Tom", "4111111111111111", "$1000"],
              ["Add", "Lisa", "5454545454545454", "$3000"],
              ["Add", "Quincy", "1234567890123456", "$2000"],
              ["Charge", "Tom", "$500"],
              ["Charge", "Tom", "$800"],
              ["Charge", "Lisa", "$7"],
              ["Credit", "Lisa", "$100"],
              ["Credit", "Quincy", "$200"]]))

# ccProvider(operations) = [["Lisa", "$-93"],
#                                   ["Quincy", "error"],
#                                   ["Tom", "$500"]]