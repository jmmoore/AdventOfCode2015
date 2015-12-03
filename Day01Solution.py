#!/usr/local/bin/python3

import os

def ParenthesisInterpreter(file):
    floor = 0
    resultList = list(open(file).read())
    for index, char in enumerate(resultList, start=1):
            if not char:
                break
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
                if floor == -1:
                    print("Hit first basement at position " + str(index) + "!")
    return floor
    
#Execution

pathToInput = os.path.abspath("/Users/JMMoore/santafloor")
floorToSendSanta = ParenthesisInterpreter(pathToInput)
print("Santa should go to floor " + str(floorToSendSanta) + "!")
