#!/usr/local/bin/python3

import operator
import os

def setUpMovementLists(file):
    movementList = list(open(file).read())
    santaMovementList = movementList[::2]
    roboSantaMovementList = movementList[1::2]
    return movementList, santaMovementList, roboSantaMovementList
    
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
movementList, santaMovementList, roboSantaMovementList = setUpMovementLists(inputFile)

#Part 1
lastYearRecord = executeMovementList(movementList)
lastYearUniqueHouses = len(set(lastYearRecord))
print("Last year, Santa visited " + str(lastYearUniqueHouses) + " unique houses!")

#Part 2 
santaRecord = executeMovementList(santaMovementList)
santaHouses = len(set(santaRecord))
roboRecord = executeMovementList(roboSantaMovementList)
roboHouses = len(set(roboRecord))
uniqueHouses = len(set(santaRecord + roboRecord))

print("Santa visited " + str(santaHouses) + " houses this year!")
print("RoboSanta visited " + str(roboHouses) + " houses this year!")
print("Together, they visited " + str(uniqueHouses) + " unique houses.")
print(str(santaHouses + roboHouses - uniqueHouses) + " lucky homes got visits from both Santa and RoboSanta!")