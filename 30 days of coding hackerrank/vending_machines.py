#!/bin/python3

import math
import os
import random
import re
import sys



class VendingMachine:
    # Implement the VendingMachine here
    def __init__(self, num_items, item_coins):
        self.num_items = num_items
        self.item_coins = item_coins
    def buy(self, num_items, item_coins):
        if num_items > self.num_items:
            raise ValueError("Not enough items in the machine")
        total_cost = num_items * self.item_coins
        if num_coins < total_cost:
            raise ValueError("Not enough coins")
            
        self.num_items -= num_items
        return num_coins - total_cost
            
    pass

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    num_items, item_coins = map(int, input().split())
    machine