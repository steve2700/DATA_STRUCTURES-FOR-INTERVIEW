#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverse_words_order_and_swap_cases(sentence):
    # Write your code here
    #split the sentence into words and reverse them 
    words = sentence.split()
    reversed_words = words[::-1]
    
    swapped_sentence = ""
    for char in reversed_words:
        swapped_sentence += char.swapcase() + " " 
        
    # return and remove the trailing space 
    return swapped_sentence.strip()
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
