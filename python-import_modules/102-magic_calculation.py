#!/usr/bin/python3
def magic_calculation(a, b):
    """Implements the bytecode.

    Args:
        a: integer
        b: integer

    Returns:
        The return value id:
            add(c, i) if TRUE
            sub(a, b) if FALSE

    """
    from magic_calculation_102 import add, sub
    if (a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return (c)
    else:
        return(sub(a, b))
