#!/usr/bin/python3
if __name__ == "__main__":
    """prints the result of the addition of all arguments

    Args:
        system arguements

    Returns:
        There is no return value
    """
    import sys
    sum_of_arguments = 0
    for argNo in range(len(sys.argv) - 1):
        sum_of_arguments += int(sys.argv[argNo + 1])
    print("{:d}".format(sum_of_arguments))
