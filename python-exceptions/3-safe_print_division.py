#!/usr/bin/python3
def safe_print_division(a, b):
    """Returns the division

    Args:
        a: int
        b: int

    Returns:
        division (a / b)
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
