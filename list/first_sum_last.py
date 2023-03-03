#Write a program that takes a list of integers and returns the sum of #the first and last numbers in the list. The original list should #remain unchanged.
#Filename: first_last_sum.py
#Example Input: [3, 6, 9, 12, 15]
#Expected Output: 18

def first_last(numbers):
    return numbers[0] + numbers[-1]
input_list = [3, 6, 9, 12, 15] 
new_list = first_last(input_list)
print(new_list)
