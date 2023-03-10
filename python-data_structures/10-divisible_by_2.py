#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list
    """
    new_list = []
    for num in my_list:
        if num % 2:
            new_list = new_list + [False]
        else:
            new_list = new_list + [True]
    return (new_list)
