#!/usr/local/bin/python3

import os

def calculatePaperNeeded(box):
    low = box[0]
    medium = box[1]
    high = box[2]
    surfaceArea = 2 * low * medium + 2 * medium * high + 2 * high * low
    slack = low * medium
    paperNeeded = surfaceArea + slack
    return paperNeeded
    
def calculateRibbonNeeded(box):
    low = box[0]
    medium = box[1]
    high = box[2]
    ribbonMath = 2 * low + 2 * medium
    bowMath = low * medium * high
    totalRibbon = ribbonMath + bowMath   
    return totalRibbon 
        
def inputSanitizer(inputFile):
    listOfBoxes = []
    inputList = open(inputFile).readlines()
    for line in inputList:
        cleanLine = line.strip('\n')
        stringBox = cleanLine.split("x")
        intBox = [int(i) for i in stringBox]
        orderedBox = sorted(intBox)
        listOfBoxes.append(orderedBox)
    return listOfBoxes
    
def allTogetherNow(listOfBoxes):
    totalPaperNeeded = 0
    totalRibbonNeeded = 0
    for box in listOfBoxes:
        paperNeeded = calculatePaperNeeded(box)
        ribbonNeeded = calculateRibbonNeeded(box)
        totalRibbonNeeded += ribbonNeeded
        totalPaperNeeded += paperNeeded
    return totalPaperNeeded, totalRibbonNeeded

# Execution

inputFile = os.path.abspath("./elfpaper")
listOfBoxes = inputSanitizer(inputFile)
result = allTogetherNow(listOfBoxes)
print("The elves need " + str(result[0]) + " feet of paper and " + str(result[1]) + " feet of ribbon, accounting for slack and bows.")
