#!/usr/bin/python3
'''
prints a text with
2 new lines after each of
these characters: ., ?
'''


def text_indentation(text):
    """
    prints a new line after this chars, . ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[i])
            print()
        else:
            if text[i - 1] in ".?:" or text[i - 1] == " " and text[i] == " ":
                continue
            print(text[i], end="")
