

def max_subarray(nums):
	max_sum = nums[0]

	for idx, num in enumerate(nums):
		current_sum = num

		if current_sum > max_sum:
			max_sum = current_sum

		for num2 in nums[idx+1::]:
			current_sum = current_sum + num2

			if current_sum > max_sum:
				max_sum = current_sum

	return max_sum


