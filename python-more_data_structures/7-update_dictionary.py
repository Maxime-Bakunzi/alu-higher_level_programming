#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """replaces/adds key/value in a dictionary

    Args:
        a_dictionary: dictionary
        key: key
        value: value

    Returns:
        Returns dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
