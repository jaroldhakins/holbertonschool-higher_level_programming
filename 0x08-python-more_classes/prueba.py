#!/usr/bin/python3
string = ""
for i in range(10):
    for j in range(10):
        string = string + "#"
    if i != 9:
        string = string + '\n'
print(string)
