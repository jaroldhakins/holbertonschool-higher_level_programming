#!/usr/bin/python3
def infinite_add(argv):
    args = len(argv) - 1
    if args == 0:
        print("0")
        return
    else:
        i = 1
        res = 0
        while i <= args:
            res = res + int(argv[i])
            i += 1
    print("{:d}".format(res))


if __name__ == "__main__":
    import sys
    infinite_add(sys.argv)
