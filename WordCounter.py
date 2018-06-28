__author__ = "Jesus"

import argparse
import re

def line_counter():
    encode = "UTF8"
    file = open(args.name,'r+',encoding = encode)
    eof = '\n'
    lines = re.findall(eof,file.read())
    lines_number = len(lines)
    file.close()
    return lines_number

def word_counter():
    encode = "UTF8"
    words_number = 0
    for line in open(args.name, 'r+', encoding=encode):
        words = re.findall(r'\S+', line)
    words_number = len(words) + words_number
    return words_number

def char_counter():
    encode = "UTF8"
    chars_number = 0
    for line in open(args.name, 'r+', encoding=encode):
        chars = re.findall('\r', line) + re.findall('\n', line) + re.findall('\s', line) + re.findall('\S', line)
        chars_number = len(chars) + chars_number
    return chars_number



parser = argparse.ArgumentParser()

parser.add_argument("file", type=str, help="Name of the file")
parser.add_argument("-lc", action="store_true", help="Number of lines in the file")
parser.add_argument("-wc", action="store_true", help="Number of words in the file")
parser.add_argument("-cc", action="store_true", help="Number of characters in the file")

args = parser.parse_args()

print("Name of the file: ",args.file)
if args.wc:
    print("Number of words: ", word_counter())
elif args.cc:
    print("Number of characters: ", char_counter())
elif args.lc:
    print("Number of lines: ", line_counter())












