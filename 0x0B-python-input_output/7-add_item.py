#!/usr/bin/python3
"""
This is a script that adds
all arguments to a python file
"""
import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    lista = load_from_json_file(filename)
except FileNotFoundError:
    lista = []
finally:
    for i in sys.argv[1:]:
        lista.append(str(i))
    save_to_json_file(lista, filename)
