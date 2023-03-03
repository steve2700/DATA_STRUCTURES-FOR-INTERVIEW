#Write a program that takes a list of strings and returns a new list #with only the strings that are longer than 5 characters. The #original list should remain unchanged.
#Filename: long_strings.py
#Example Input: ['cat', 'dog', 'fish', 'bird', 'elephant']
#Expected Output: ['elephant']

def long_strings(strings):
    return [word for word in strings if len(word) >= 5]
    
    
input_list = ['cat', 'dog', 'fish' , 'bird', 'elephant']
new_list =long_strings(input_list)
print(new_list)

