#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #Given a base-10 integer, n, convert it to binary (base-2)
    binary_num = bin(n)[2:]
    #Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation.
    count = 0
    max_count = 0
    for digit in binary_num:
        if digit == '1':
            count = count + 1
        else:
            count = 0
        max_count = max(max_count, count)
    print(max_count)
        
            
        
            
            
