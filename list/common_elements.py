#Write a program that takes two lists of integers and returns a new list #with the elements that are common to both lists. The original lists #should remain unchanged.
#Filename: common_elements.py
#Example Input: [1, 2, 3, 4, 5], [3, 5, 7, 9, 11]
#Expected Output: [3, 5]

def common_elements(list1, list2):
    return [x for x in list1 if x in list2 ]
    
    
input_list1 = [1, 2, 3, 4, 5]
input_list2 = [3, 5, 7, 9, 11]
new_list = common_elements(input_list1, input_list2)
print(new_list)


