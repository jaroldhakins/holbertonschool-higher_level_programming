#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return None
    max_value = max(a_dictionary.values())
    for i, j in a_dictionary.items():
        if j == max_value:
            return i
