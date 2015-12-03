#!/usr/local/bin/python3

# >>> line = '1234567890'
# >>> n = 2
# [line[i:i+n] for i in range(0, len(line), n)]
# ['12', '34', '56', '78', '90']

import operator
import os

def setUpMovementLists(file):
    movementList = list(open(file).read())
    santaMovementList = movementList[::2]
    roboSantaMovementList = movementList[1::2]
    return santaMovementList, roboSantaMovementList
    
def executeMovementList(movementList):
    initialPosition = (0, 0)
    moveUp = (0, 1)
    moveDown = (0, -1)
    moveRight = (1, 0)
    moveLeft = (-1, 0)
    recordOfMovement = [initialPosition]
    for char in movementList:
        if char == "^":
            initialPosition = tuple(map(operator.add, initialPosition, moveUp))
            recordOfMovement.append(initialPosition)
        elif char == "v":
            initialPosition = tuple(map(operator.add, initialPosition, moveDown))
            recordOfMovement.append(initialPosition)
        elif char == "<":
            initialPosition = tuple(map(operator.add, initialPosition, moveLeft))
            recordOfMovement.append(initialPosition)
        elif char == ">":
            initialPosition = tuple(map(operator.add, initialPosition, moveRight))
            recordOfMovement.append(initialPosition)
    return recordOfMovement

# Execution

inputFile = os.path.abspath("/Users/JMMoore/santaPath") 
santaMovementList, roboSantaMovementList = setUpMovementLists(inputFile)
santaRecord = executeMovementList(santaMovementList)
roboRecord = executeMovementList(roboSantaMovementList)
uniqueHouses = len(set(santaRecord + roboRecord))
print(uniqueHouses)