#!/usr/bin/env python3

import random

def print_matrix(n, m):
    for i in range(n):
        for j in range(m):
            random_number = random.randint(20, 80)
            print('{:<4}'.format(random_number), end="")
        print()

rows = 5
columns = 10

print_matrix(rows, columns)
