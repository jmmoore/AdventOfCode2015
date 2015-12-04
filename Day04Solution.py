#!/usr/local/bin/python3

import os
import sys
import hashlib

def findLowestNZeroHash(secretKey, numberOfZeroes):
    suffix = 0
    # I would like to not have to cast this in the program at all, but not sure how to do that when it's passed in as an argument
    numberOfZeroes = int(numberOfZeroes)
    while True:
        puzzleInput = secretKey + str(suffix)
        hashed = hashlib.md5(puzzleInput.encode('utf-8')).hexdigest()
        if hashed[0:numberOfZeroes] != ("0" * numberOfZeroes):
            suffix += 1
            continue
        else:
            return(suffix)

#Execution
if len(sys.argv) <=1:
    print("Solution requires two parameters: secret Key, and number of zeroes to solve for. exiting.")
    exit(1)
secretKey = sys.argv[1]
numberOfZeroes = sys.argv[2]
solution = findLowestNZeroHash(secretKey, numberOfZeroes)
print(solution)