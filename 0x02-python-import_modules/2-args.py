#!/usr/bin/python3
def arguments(argv):
    num_args = len(argv) - 1
    if num_args == 0:
        print("{:d} arguments.".format(num_args))
        return
    else:
        if num_args == 1:
            print("{:d} argument:".format(num_args))
        else:
            print("{:d} arguments:".format(num_args))
        i = 1
        while i <= num_args:
            print("{:d}: {:s}".format(i, argv[i]))
            i += 1

if __name__ == "__main__":
    import sys
    arguments(sys.argv)
