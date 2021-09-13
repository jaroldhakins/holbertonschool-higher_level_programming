#!/usr/bin/python3
def arguments(argv):
    num_arg = len(argv) - 1
    if num_arg == 0:
        print("0 arguments")
    elif num_arg == 1:
        print("1 argument")
    elif num_arg > 1:
        print("{:d} argument".format(num_arg))
    i = 1
    while i <= num_arg:
        print("{:d}: {:s}".format(i, argv[i]))
        i = i + 1

if __name__ == "__main__":
    import sys
    arguments(sys.argv)
