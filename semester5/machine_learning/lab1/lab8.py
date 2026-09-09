#!/usr/bin/env python3

import random

def print_matrix(n):
    for i in range(n):
        for j in range(n):
            char = '*'
            print('{:<2}'.format(char), end="")
        print()

matrix_size = int(input("matrix size: "))
print_matrix(matrix_size)