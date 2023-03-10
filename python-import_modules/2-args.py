#!/usr/bin/python3
if __name__ == "__main__":
    """Prints the number of and the list of its arguments

    Args:
        system arguments

    Returns:
        There is no return value
    """
    import sys
    no_of_arguments = len(sys.argv) - 1
    if (no_of_arguments == 0):
        print("0 arguments.")
    elif (no_of_arguments == 1):
        print("1 argument:")
    else:
        print("{:d} arguments:".format(no_of_arguments))
    for argNo in range(no_of_arguments):
        print("{}: {}".format(argNo + 1, sys.argv[argNo + 1]))
