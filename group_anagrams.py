
import collections

def groupAnagrams(my_list):
   
    word_key_dict = {}
    
    for word in my_list:
        sorted_word = "".join(sorted(word))
        word_key_dict[sorted_word] = word_key_dict.get(sorted_word, []) + [word]
  

    print (word_key_dict.values())
    return word_key_dict.values()

 

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])       
    

def groupAnagrams2(strs):
#alt solution given

    # ans = collections.defaultdict(list)
    # for s in strs:
    #     count = [0] * 26
    #     for c in s:
    #         count[ord(c) - ord('a')] += 1
    #     ans[tuple(count)].append(s)
    #     print(ans)

    # return ans.values()

    output_dict = collections.defaultdict(list)
    for string in strs:
        _hash = [0] * 26

        for char in string:
            _hash[ord(char) - ord('a')] += 1
            output_dict[tuple(_hash)].append(string)

        print (output_dict)
        print (output_dict.values())

groupAnagrams2(["eat", "tea", "tan", "ate", "nat", "bat"])     