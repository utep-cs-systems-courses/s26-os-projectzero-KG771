import os
import re

def file_reader(input_file):
    #input files can be read only (os.O_RDONLY)
    fd = os.open(input_file, os.O_RDONLY)
    #print("Input file fd: ", fd)
    
    info = os.read(fd, 17138)
    print("File reader info:", info)

def file_writer(output_file, dictionary):
    #output file can be write-only, created, or overwritten (if it exists)
    fd = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    #print("Output file fd: ", fd)

    for key in dictionary:
        string = f"{key} {dictionary[key]}"
        strToBytes = string.encode("utf-8")
        os.write(fd, strToBytes)

def word_count(words):
    wordCounts = {}
    for word in words:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1


file_reader("declaration.txt")
file_writer("output.txt")

