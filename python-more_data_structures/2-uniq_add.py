#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all uniq integers in a list

    Args:

    Returns:
        returns the sum of uniq integers
    """
    sum = 0
    for num in set(my_list):
        sum += num
    return sum
