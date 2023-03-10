#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """replaces an element tn a list at a
    specific position withoit modifying the
    original list.
    """
    if (idx < 0 or idx > (len(my_list) - 1)):
        return my_list
    else:
        new = [num for num in my_list]
        new[idx] = element
        return(new)
