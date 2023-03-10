#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer

    If a ValueError message is caught, a corresponding
    message is printed to standard error

    Args:
        value: int

    Returns:
        True: TypeError or ValueError
        otherwise: False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError) as err:
        sys.stderr.write("Exception: " + str(err) + '\n')
        return (False)
