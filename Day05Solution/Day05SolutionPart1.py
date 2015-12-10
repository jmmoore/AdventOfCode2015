#!/usr/local/bin/python3

import os

def areThereEnoughVowels(string, array):
      vowelCount = 0
      for letter in string:   
          if letter in array:
              vowelCount += 1
      if vowelCount < 3:
          return False
      else:
          return True

def isArrayItemInString(string, array):
    if any(substring in string for substring in array): 
        return True
    else:
        return False

# Execution

inputFile = os.path.abspath("./Day05Input")
doubleLetters = set(['aa','bb','cc','dd','ee','ff','gg','hh','ii','jj','kk','ll','mm','nn','oo','pp','qq','rr','ss','tt','uu','vv','ww','xx','yy','zz'])
vowelSet = ['a','e','i','o','u']
naughtySubStrings = set(['ab','cd','pq','xy'])
inputList = list(open(inputFile).readlines())
niceCounter = 0

for item in inputList:
        if isArrayItemInString(item, naughtySubStrings):
            continue
        if areThereEnoughVowels(item, vowelSet):
            if isArrayItemInString(item, doubleLetters):
                niceCounter += 1

print(niceCounter)
