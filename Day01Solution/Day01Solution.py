#!/usr/local/bin/python3

import os

def ParenthesisInterpreter(inputFile):
    firstBasement = None
    floor = 0
    resultList = list(open(inputFile).read())
    for index, char in enumerate(resultList, start=1):
        if not char:
            break
        if char == "(":
            floor += 1
        elif char == ")":
            floor -= 1
        if floor == -1 and not firstBasement:
            print("Hit basement for the first time at position " + str(index) + "!")
            firstBasement = True
    return floor
    
#Execution

pathToInput = os.path.abspath("./santafloor")
floorToSendSanta = ParenthesisInterpreter(pathToInput)
print("Santa should go to floor " + str(floorToSendSanta) + "!")
