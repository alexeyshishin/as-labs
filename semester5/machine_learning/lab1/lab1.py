#!/usr/bin/env python3

string = "Pyth1abch2hon"

first_h = string.find('h')
last_h = string.rfind('h')

if first_h != -1 and last_h != -1 and first_h != last_h:
    start = string[:first_h + 1]
    middle_reversed = string[first_h + 1:last_h][::-1]
    end = string[last_h:]
    new_string = start + middle_reversed + end
else:
    new_string = string

print(new_string)
