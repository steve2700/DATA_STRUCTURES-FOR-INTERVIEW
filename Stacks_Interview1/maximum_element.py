#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#

def getMax(operations):
    '''1 x  -Push the element x into the stack.'''

    stack = []
    max_values = []
    for operation in operations:
        if operation.startswith('1'):
            _, x = operation.split()
            x = int(x)
            stack.append(x)
        #2 -Delete the element present at the top of the stack.'''
        elif operation == '2':
            if stack:
                stack.pop()
        
        #3 -Print the maximum element in the stack.
        elif operation == '3':
            if stack:
                max_values.append(max(stack))
    return(max_values)
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
