#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    """Returns a new value multiplied by 2

    Args:
        a_dictionary: dictionary

    Returns:
        integer.
    """
    return {key: num * 2 for key, num in a_dictionary.items()}
