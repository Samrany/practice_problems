#brute solution
def twoSum(nums, target):
        
    length = len(nums)
    
    for idx in range(length):
        for idx2 in range(idx+1, length):
                if nums[idx] + nums[idx2] == target:
                    print(idx, idx2)
                    return[idx, idx2]

#two-pass hash solution
def twoSum2(nums, target):
    hash_table = {}

    for idx in range(len(nums)):
        hash_table[nums[idx]] = idx

    for idx in range(len(nums)):
        match = target - nums[idx]
        if match in hash_table and hash_table[match] != idx:
            
            return [idx, hash_table[match]]

    return []


#one-pass hash solution
def twoSum3(nums, target):

    hash_table = {} 

    for idx, val in enumerate(nums):
        match = target - val 

        if match in hash_table and hash_table[match] !=  idx: 
            return[idx, hash_table[match]]

        hash_table[val] = idx

    return []


print(twoSum3([0, 2, 5, 8, 3, 5, 2], 4))
print(twoSum3([0, 3, 6], 4))