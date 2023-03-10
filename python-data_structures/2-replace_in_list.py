#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element of a list at specific position
    """
    if ((idx < 0) or idx > (len(my_list) - 1)):
        return (my_list)
    else:
        if my_list[idx]:
            my_list[idx] = element

        return my_list
