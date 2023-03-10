#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """adds two tuples

    Args:
        tuple_a: integer
        tuple_b: integer

    Returns:
        A tuple with 2 integers.
        - first element should be the addition
            of the first element of each argument
        - Second element should be the addition
            of the second element of each argument
    if len(tuple_a) < 2:
        if len(tuple_a == 0):
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    """
    tuple_a += (0, 0)
    tuple_b += (0, 0)

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
