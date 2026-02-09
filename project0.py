import os
import re

def file_reader(input_file):
    #input files can be read only (os.O_RDONLY)
    fd = os.open(input_file, os.O_RDONLY)
    #print("Input file fd: ", fd)
    
    info = os.read(fd, 17138)
    bytesToStr = info.decode("utf-8")
    
    os.close(fd)

    return bytesToStr


def file_writer(output_file, dictionary):
    #output file can be write-only, created, or overwritten (if it exists)
    fd = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC)
    #print("Output file fd: ", fd)

    for key in dictionary:
        string = f"{key} {dictionary[key]}\n"
        strToBytes = string.encode("utf-8")
        os.write(fd, strToBytes)

    os.close(fd)


def extract_words(string):
    #converts all characters to lowercase
    lowerStr = string.lower()
    #extracts words
    words = re.findall(r"\b\w+\b", lowerStr)

    return words


def word_count(string):
    words = extract_words(string)

    #initializes and populates dictionary
    wordCounts = {}
    for word in words:
        if word not in wordCounts:
            wordCounts[word] = 1
        else:
            wordCounts[word] += 1
    return wordCounts


string = file_reader("declaration.txt")
file_writer("output.txt")
word_count(string)

