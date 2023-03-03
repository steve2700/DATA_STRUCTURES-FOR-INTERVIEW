#Write a program that takes a list of numbers and returns a new list #with the numbers sorted in ascending order. The original list #should remain unchanged.

#Filename: sort_numbers.py

#Example Input: [5, 3, 8, 1, 2]
#Expected Output: [1, 2, 3, 5, 8]

def sort_numbers(numbers):
    return sorted(numbers)
    
input_list = [5, 3, 8, 1, 2]
new_list = sort_numbers(input_list)
print(new_list)
