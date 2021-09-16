#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = map(lambda i: replace if i is search else i, my_list)
    return list(new_list)
