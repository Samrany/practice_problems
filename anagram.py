def isAnagram(s: str, t: str) -> bool:
    
    if len(s) != len(t):
        return False
    else:
        char_count = {}
        for char in s:
            char_count[char] = char_count.get(char, 0) + 1

        for char in t:
            if char in char_count:
                char_count[char] = char_count[char] - 1

            else:
                return False

        nums = char_count.values()
        
        for num in nums:
            if num != 0:
                return False

        else:
            return True   






