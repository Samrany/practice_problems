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
	
	for num in nums:
		product = num * product 

	for num in nums:
		output_list.append(int(product / num))

	return output_list



print(Product_except_self2([1, 2, 3]) )
#print(Product_except_self([1, 2, 4]) )

# 6, 3, 2
# 8, 4, 2