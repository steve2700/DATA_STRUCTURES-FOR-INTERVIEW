#Write a program that takes a list of integers and returns a new list #with only the even numbers. The original list should remain #unchanged.
#Filename: even_numbers.py
#Example Input: [3, 5, 6, 8, 9, 10, 11, 12, 15]
# Output: [6, 8, 10, 12]

def even_numbers(numbers):
    return[num for num in numbers if num % 2 == 0]
    
    
input_list = [3, 5, 6, 8, 9, 10, 11, 12, 15]
result_list = even_numbers(input_list)
print(result_list)
