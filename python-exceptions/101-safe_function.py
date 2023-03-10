#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    """Executes a file safely

    Args:
        fct: function to execute
        args: fct arguments

    Returns:
        None: if there's an error
        otherwise: results of the call to fct
    """
    try:
        return fct(*args)
    except ZeroDivisionError:
        print("Exception: division by zero", file=sys.stderr)
    except IndexError:
        print("Exception: list index out of range", file=sys.stderr)
    return None
