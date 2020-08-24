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


def median_sorted_arrays(list1, list2):

    evaluation_array = []
    pointer1 = 0
    pointer2 = 0

    while len(evaluation_array) < len(list1) + 1:

        if list1[pointer1] < list2[pointer2]:
            evaluation_array.append(list1[pointer1])
            pointer1 += 1

        else:
            evaluation_array.append(list2[pointer2])
            pointer2 += 1

    num1, num2 = evaluation_array[-1], evaluation_array[-2]

    return (num1 + num2) / 2    


print(median_sorted_arrays([1, 2, 8],[5, 6, 7]))
# pointer can get out of range