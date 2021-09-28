#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        total = a / b
        print("Inside result: {:.1f}".format(total))
    except:
        total = None
        print("Inside result: {}".format(total))
    finally:
        return total
