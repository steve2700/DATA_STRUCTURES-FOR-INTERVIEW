#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    #first we read the integer
    n = int(input().strip())
    #check the range range of multiples of 10
    for i in range(1, 11):
        #finally we print in the format of n x i = n*i 
        print(n, 'x', i, '=', n*i)
