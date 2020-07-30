
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
    my_dict = {}
    value_set = set()
    
    for word in my_list:
        my_dict[word] = {}
        
        for char in word:
            my_dict[word][char] = my_dict[word].get(char,0) + 1
            
        # value_set.add(my_dict[word])

    print(my_dict)
    print(value_set)
 

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])       
    
    # for item in value_set:
    #     group_list = []
    #     #get key where value is equal

    #     group_list.append(match)
    #     output
    # dict.
                    
    # extract the values into a set
    # loop over set and for each item
    #     add keys with that value to a list to output