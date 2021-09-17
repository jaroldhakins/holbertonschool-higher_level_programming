#!/usr/bin/python
def roman_to_int(roman_string):
    Dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    num = 0
    for i in range(len(roman_string)):
        if i > 0 and Dict[roman_string[i]] > Dict[roman_string[i - 1]]:
            num += Dict[roman_string[i]] - 2 * Dict[roman_string[i - 1]]
        else:
            num += Dict[roman_string[i]]
    return num
