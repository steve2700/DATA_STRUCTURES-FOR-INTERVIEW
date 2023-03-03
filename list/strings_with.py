#Write a program that takes a list of strings and returns a new list #with only the strings that start with the letter 'a'. The original #list should remain unchanged.

#Filename: strings_starting_with_a.py

#Example Input: ['cat', 'dog', 'apple', 'bird', 'ant']
#Expected Output: ['apple', 'ant']

def strings_with_a(strings):
    return [word for word in strings if word.startswith ('a') ]
    
input_list = ['cat', 'dog', 'apple', 'bird', 'ant']
new_list = strings_with_a(input_list)
print(new_list)
