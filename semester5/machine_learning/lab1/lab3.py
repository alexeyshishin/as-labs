#!/usr/bin/env python3

array_size = int(input("array size: "))
array_elements = list(map(int, input("array elements: ").split()))

temp = array_elements[0]
array_elements[0] = array_elements[-1]
array_elements[-1] = temp

print("reversed array:", array_elements)