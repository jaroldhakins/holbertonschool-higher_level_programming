#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for j, i in enumerate(my_list):
        if i % 2 == 0:
            new_list[j] = True
        else:
            new_list[j] = False
    return new_list
