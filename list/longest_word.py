#Write a program that takes a list of words and returns the length of #the longest word in the list. The original list should remain #unchanged.
#Filename: longest_word.py
#Example Input: ['apple', 'banana', 'orange', 'watermelon', 'pineapple']
#Expected Output: 10 

def longest_word(words):
    max_length = 0
    for word in words:
        
        if len(word) > max_length:
            max_length = len(word)
        
        
    return max_length
    
    
    
input_list = ['apple', 'banana', 'orange', 'watermelon', 'pineapple']
new_list = longest_word(input_list)
print(new_list)




