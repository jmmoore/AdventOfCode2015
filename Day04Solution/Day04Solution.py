#!/usr/local/bin/python3

import sys
import hashlib

def findLowestNZeroHash(secretKey, numberOfZeroes):
    suffix = 0
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
secretKey = open(sys.argv[1]).read()
secretStrip = secretKey.strip('\n')
numberOfZeroes = sys.argv[2]
print(secretStrip)
solution = findLowestNZeroHash(secretStrip, numberOfZeroes)
print(solution)
