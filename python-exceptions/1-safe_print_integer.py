#!/usr/bin/python3
def safe_print_integer(value):
    """Print the first x elements of a list that are integers.

    Args:
        my_list: list to print elements from
        x: The number of elements of my_list to print.

    Returns:
        The number of elements printed.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
