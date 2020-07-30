
def groupAnagrams(my_list):
   
    word_key_dict = {}
    
    for word in my_list:
        sorted_word = "".join(sorted(word))
        word_key_dict[sorted_word] = word_key_dict.get(sorted_word, []) + [word]
  

    print (word_key_dict.values())
    return word_key_dict.values()

 

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])       
    
