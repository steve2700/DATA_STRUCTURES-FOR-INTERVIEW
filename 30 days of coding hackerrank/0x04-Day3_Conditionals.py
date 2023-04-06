#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    #check if n is odd and print Weird
    if N % 2 == 1:
        print('Weird')
    #check if n is even and in range 2, 5 and print Not Weird
    elif N % 2 == 0 and N in range(2, 6):
        print('Not Weird')
    #check if n is even and in range 6,20 and print Weird
    elif N % 2 == 0 and N in range(6, 21):
        print('Weird')
    #check if n is even and is greater than 20
    elif N % 2 == 0 and N > 20:
        print('Not Weird')
    