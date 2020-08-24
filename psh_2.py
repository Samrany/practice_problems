import typing

# [3, 1, -3, 5, 6, -8, 2]

# def max_subarray(nums):
#   max_sum = nums[0]

#   for idx, num in enumerate(nums):
#       current_sum = num

#       if current_sum > max_sum:
#           max_sum = current_sum

#       for num2 in nums[idx+1::]:
#           current_sum = current_sum + num2

#           if current_sum > max_sum:
#               max_sum = current_sum

#   return max_sum



def maxSubArray(nums: typing.List[int]) -> int:
    maxSub, curSum = nums[0], 0
    
    for n in nums:
        if curSum < 0:
            curSum = 0
        curSum += n
        maxSub = max(maxSub, curSum)
    return maxSub


print(maxSubArray([8, -1, 7, 1, -4]))
# 

# n = -4
# maxSub =  15
# curSum = -4

# [-4, 3, 2, -5, 2, 5, -1]
