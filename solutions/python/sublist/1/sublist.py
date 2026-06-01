"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if len(list_one) == len(list_two):
        if list_one == list_two:
            return 3
        
    elif len(list_one) > len(list_two):
        if len(list_two) == 0:
            return 2
        length = len(list_two)
        start = 0
        while start+length <= len(list_one):
            sliced = list_one[start:start+length]
            if sliced == list_two:
                return 2
            start += 1
        
    else:
        if len(list_one) == 0:
            return 1
        length = len(list_one)
        start = 0
        while start+length <= len(list_two):
            sliced = list_two[start:start+length]
            if sliced == list_one:
                return 1
            start += 1
    
    return 4
    