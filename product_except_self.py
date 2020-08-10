# repeat problem
# example of input and output
# [1, 2, 3] => [6, 3, 2]


# ask clarifying questions
# n will always be > 1?
# strings or always integers?

# write pseudo code
# set empty list for output
# length of list 
# loop over the list:
# 		loop over all items (val and idx) except current in list:
# 			multiply together
# 			append to output list

# return output list


# code
# run through an example
# discuss runtime/if there's a better solution

def Product_except_self(nums):

	output_list = []
	length = len(nums)


	for idx, val in enumerate(nums):
		product = 1

		for idx2, val2 in enumerate(nums):
			if idx != idx2:

				product = val2 * product
				print(idx, idx2, val2, product)		
		output_list.append(product)

	return output_list	



def Product_except_self2(nums):
	output_list = []
	product = 1
	product_without_zeros = 1
	
	for num in nums:
		
		if num != 0:
			product_without_zeros = num * product_without_zeros

		product = num * product 
		


	for num in nums:
		if num == 0:
			output_list.append(product_without_zeros)

		else:
			output_list.append(int(product / num))

	return output_list


def product_third_approach(nums):
	length = len(nums)
	left_prod, right_prod, total_prod = [1]*length, [1]*length, [1]* length
	print(left_prod)


print(product_third_approach([1, 2, 3]))
print(product_third_approach([0, 2, 4])) #8, 0, 0
#print(Product_except_self([1, 2, 4]) )

# 6, 3, 2
# 8, 4, 2