import os
import re
import sys

def file_reader(input_file):
    #input files can be read only (os.O_RDONLY)
    fd = os.open(input_file, os.O_RDONLY)
    #print("Input file fd: ", fd)
    
    chunks = []
    while True:
        data = os.read(fd, 4096)   
        if not data:             
            break
        chunks.append(data)
    
    os.close(fd)

    return b"".join(chunks).decode("utf-8")


def file_writer(output_file, sorted_pairs):
    #output file can be write-only, created, or overwritten (if it exists)
    fd = os.open(output_file, os.O_WRONLY | os.O_CREAT | os.O_TRUNC , 0o644)
    #print("Output file fd: ", fd)

    for key, value in sorted_pairs:
        string = f"{key} {value}\n"
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

def sort_descending(counts):
    return sorted(counts.items(), key=lambda pair: pair[1], reverse=True)


if __name__ == "__main__":

    counts = {}
    string = file_reader(sys.argv[1])
    counts = word_count(string)
    counts = sort_descending(counts)
    file_writer(sys.argv[2], counts)


