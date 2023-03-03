#Write a program that takes a list of strings and returns a new list #with only the strings that contain the letter 'a'. The original #list should remain unchanged.
#Filename: strings_with_a.py
#Example Input: ['cat', 'dog', 'fish', 'bird', 'elephant']
#Expected Output: ['cat',  'elephant']


def strings_with_a(strings):
    
    return [word for word in strings if "a" in word]
    
    
input_string = ['cat', 'dog', 'fish', 'bird', 'elephant']
new_list = strings_with_a(input_string)
print(new_list)

