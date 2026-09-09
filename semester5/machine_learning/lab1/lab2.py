#!/usr/bin/env python3

array = [10, -7, 8, -100, -50, 32, 87, 117, -210]

print(min(array, key=abs))
print(max(array, key=abs))
print(sorted(array, key=abs))
