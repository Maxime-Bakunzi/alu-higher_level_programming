#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element

    Args:
        my_list_1: first list
        my_list_2: second list
        list_length: number of elements to divide

    Returns:
        A new list containing all the divisions
    """
    newList = []
    try:
        for elem in range(list_length):
            try:
                newList.append(my_list_1[elem] / my_list_2[elem])
            except TypeError:
                newList.append(0)
                print("wrong type")
                continue
            except ZeroDivisionError:
                print("division by 0")
                div = 0
                newList.append(div)
                continue
            except IndexError:
                print("out of range")
                div = 0
                newList.append(0)
    finally:
        return (newList)
