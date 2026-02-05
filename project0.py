import os
import re

def file_reader(file):
    #input files can be read only (os.O_RDONLY)
    fd = os.open(file, os.O_RDONLY)

file_reader("declaration.txt")

