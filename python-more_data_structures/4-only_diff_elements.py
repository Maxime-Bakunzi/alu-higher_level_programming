#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Returns a set of all elements in only one set

    Args:

    Returns:
        Set
    """
    return set(set_1 ^ set_2)
