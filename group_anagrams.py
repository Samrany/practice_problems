
def groupAnagrams(my_list):

# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]
# {"eat":{'e':1, 'a': 1, 't': 1}, "tea":{}}
   
    output_list = []
    dict = {}
    value_set = set()
    
    for each word in strs:
        dict[word] = {}
        
        for char in word:
            dict[word][char] = dict[word].get(char,0) + 1
            
        value_set.append(dict[word])
        
    
    # for item in value_set:
    #     group_list = []
    #     #get key where value is equal

    #     group_list.append(match)
    #     output
    # dict.
                    
    # extract the values into a set
    # loop over set and for each item
    #     add keys with that value to a list to output