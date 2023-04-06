
#funny!
import math
import random
import re
import os
import sys

def solve(meal_cost, tip_percent, tax_percent):
    # we need to know the tip amount and tax amount 
    tip = meal_cost * tip_percent / 100
    tax = meal_cost * tax_percent / 100

    # lets calculate the total 
    total_cost = meal_cost + tip + tax
    #lets round the total cost to the nearest integer
    print(round(total_cost))

    if __name__ == '__main___':
        meal_cost = float(input().strip())
        tip_percent = int(input().strip())
        tax_percent = int(input().strip())

        solve(meal_cost, tip_percent, tax_percent)


    










