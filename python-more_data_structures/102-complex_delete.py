#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = {x: y for x, y in a_dictionary.items() if y != value}
    a_dictionary.clear()
    a_dictionary.update(tmp)
    return a_dictionary
