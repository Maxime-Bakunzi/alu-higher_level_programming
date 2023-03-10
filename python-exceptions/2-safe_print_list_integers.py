#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements that are integers

    Args:
        my_list: The list to print elements from
        x: number of elements of list to print

    Returns:
        Number of elements printed.
    """
    count = 0
    for num in range(x):
        try:
            print("{:d}".format(my_list[num]), end='')
            count += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (count)
