#brute solution
def twoSum(nums, target):
        
    length = len(nums)
    
    for idx in range(length):
        for idx2 in range(idx+1, length):
                if nums[idx] + nums[idx2] == target:
                    print(idx, idx2)
                    return[idx, idx2]

#two-pass hash solution
def twoSum1(nums, target):
    hash_table = {}

    for idx in range(len(nums)):
        hash_table[nums[idx]] = idx

    for idx in range(len(nums)):
        match = target - nums[idx]
        if match in hash_table and hash_table[match] != idx:
            
            return [idx, hash_table[match]]

    return []


# hash_table={}
# for i in range(len(nums)):    # 先做一個hash table
#     hash_table[nums[i]]=i
# for i in range(len(nums)):
#     if target-nums[i] in hash_table:
#         if hash_table[target-nums[i]] != i:
#             return [i, hash_table[target-nums[i]]]
# return []

# public int[] twoSum(int[] nums, int target) {
#     Map<Integer, Integer> map = new HashMap<>();
#     for (int i = 0; i < nums.length; i++) {
#         map.put(nums[i], i);
#     }
#     for (int i = 0; i < nums.length; i++) {
#         int complement = target - nums[i];
#         if (map.containsKey(complement) && map.get(complement) != i) {
#             return new int[] { i, map.get(complement) };
#         }
#     }
#     throw new IllegalArgumentException("No two sum solution");
# }

# def twoSum(nums: List[int], target: int) -> List[int]:
        
#     length = len(nums)
    
#     for idx, value in enumerate(nums):
#         for idx2, value2 in enumerate(nums[idx+1:len]):
#             if value + value2 == target:
#                 return [idx, idx2]

print(twoSum([0, 2, 5, 8, 3, 5, 2], 4))
print(twoSum([0, 3, 6], 4))