def twoSum(nums, target):
        
    length = len(nums)
    
    for idx in range(length):
        for idx2 in range(idx+1, length):
                if nums[idx] + nums[idx2] == target:
                    print(idx, idx2)
                    return[idx, idx2]


# def twoSum(nums: List[int], target: int) -> List[int]:
        
#     length = len(nums)
    
#     for idx, value in enumerate(nums):
#         for idx2, value2 in enumerate(nums[idx+1:len]):
#             if value + value2 == target:
#                 return [idx, idx2]

twoSum([0, 2, 5, 8, 3, 5, 2], 4)
