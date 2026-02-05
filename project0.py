import os
import re

def file_reader(file):
    fd = os.open(file, os.O_RDONLY)

file_reader("declaration.txt")

