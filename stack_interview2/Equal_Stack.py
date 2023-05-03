#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    # Find the initial height of each stack
    height1, height2, height3 = sum(h1), sum(h2), sum(h3)
    max_height = max(height1, height2, height3)

    # Keep removing the top element from the stack with the highest height until all three stacks have the same height
    while height1 != height2 or height2 != height3:
        if height1 == max_height:
            height1 -= h1.pop(0)
        elif height2 == max_height:
            height2 -= h2.pop(0)
        elif height3 == max_height:
            height3 -= h3.pop(0)

        max_height = max(height1, height2, height3)

    # Return the height of the stacks once they are all equal
    return max_height

    
            
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n1 = int(first_multiple_input[0])

    n2 = int(first_multiple_input[1])

    n3 = int(first_multiple_input[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
