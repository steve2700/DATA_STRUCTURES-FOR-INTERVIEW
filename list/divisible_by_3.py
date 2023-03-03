#Write a program that takes a list of numbers and returns a new list #with only the numbers that are divisible by 3. The original list #should remain unchanged.
#Filename: divisible_by_3.py
#Example Input: [1, 3, 5, 9, 12, 15, 20]
#Expected Output: [3, 9, 12, 15]


def divisible_by_3(numbers):
    return [x for x in numbers if x % 3 == 0]
    
input_list = [1 , 3 , 5, 9, 12, 15, 20]
new_list = divisible_by_3(input_list)
print(new_list)

