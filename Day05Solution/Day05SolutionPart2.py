#!/usr/local/bin/python3

import os

def checkForDuplicatePattern(string):
    i = 0
    while i < len(string):
        a, b = 0, 2
        checkString = string[(a+i):(b+i)]
        if string.count(checkString) > 1 and len(checkString) > 1:
                return True
                i += 1
    return False

def checkForSeparatedRepeats(string):
    for char in string:
        if char*2 in string[::2] or char*2 in string[1::2]:
                return True
        else:
                continue
    return False

def countNiceStrings(inputFile):
    inputList = list(open(inputFile).readlines())
    niceCounter = 0
    for string in inputList:
        if checkForDuplicatePattern(string) and checkForSeparatedRepeats(string):
            niceCounter += 1
            else:
            continue
    return niceCounter

# Execution

inputFile = os.path.abspath("./Day05Input")
niceStringsCount = countNiceStrings(inputFile)
print(niceStringsCount)
