#!/usr/bin/python3

"""
Script that adds all arguments to a Python list and saves them to a JSON file.
"""

from sys import argv
import importlib
import os

module0 = importlib.import_module('5-save_to_json_file')
module1 = importlib.import_module('6-load_from_json_file')

filename = "add_item.json"

if os.path.exists(filename):
    my_list = module1.load_from_json_file(filename)
else:
    my_list = []

my_list.extend(argv[1:])

module0.save_to_json_file(my_list, filename)
