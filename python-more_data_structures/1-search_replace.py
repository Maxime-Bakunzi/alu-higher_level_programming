#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """Replaces all occurences of an element by
    another in a new list

    Args:

    Returns:
        Returns a new list.
    """
    new = [num if num != search else replace for num in my_list]
    return (new)
