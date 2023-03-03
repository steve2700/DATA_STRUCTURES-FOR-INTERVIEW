#Write a program that takes a list of words and returns a new list with #the words sorted in alphabetical order. The original list should #remain unchanged.
#Filename: sort_words.py
#Example Input: ['cat', 'dog', 'fish', 'bird', 'elephant']
#Expected Output: ['bird', 'cat', 'dog', 'elephant', 'fish']

def sorted_words(words):
    return sorted(words)
    
input_list = ['cat', 'dog', 'fish', 'bird', 'elephant']
new_list = sorted_words(input_list)
print(new_list)
