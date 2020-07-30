
def groupAnagrams(my_list):
   
    output_list = []
    word_key_dict = {}
    
    for word in my_list:
        sorted_word = "".join(sorted(word))
        word_key_dict[sorted_word] = word_key_dict.get(sorted_word, []) + [word]
  
    for key, value in word_key_dict.items():
        print(value)

 

groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])       
    
