import math
import os
import random
import re
import sys

def mostActive(customers):
    freq = {}
    n = len(customers)
    for c in customers:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    active = []
    for c in freq:
        if freq[c] / n >= 0.05:
            active.append(c)
    return sorted(active)

if __name__ == '__main__':
    customers_count = int(input().strip())

    customers = []

    for _ in range(customers_count):
        customers_item = input()
        customers.append(customers_item)

    result = mostActive(customers)

    print('\n'.join(result))
