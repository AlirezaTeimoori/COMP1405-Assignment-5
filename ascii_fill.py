'''
    -- Created by:     Alireza Teimoori  --
    -- Created on:     Dec 2 2019        --
    -- Created for:    Assignment 5      --
    -- Course Code:    COMP1405          --
    -- Teacher Name:   Andrew Runka      --
    '''

def readLevel(levelNumber:int): # This function gets the level number and reads that level

    levelName = f"./levels/ascii_level{str(levelNumber)}.txt" # Create level name using the input number

    with open(levelName,"r") as levelFile: # Opens the file AND CLOSES the file when got out of indentation

        levelString = levelFile.read() # Read the whole file into a single string
        gameBoard = [[char for char in string] for string in levelString.split("\n")] # Split the rows that are the splited form of the big string
        
    return gameBoard

def displayBoard(gameBoard:list): # This function takes a gameBoard and displays it to the console

    nLst = [str(i)[-1] for i in range(len((gameBoard[0])))]
    print("   "+"".join(nLst))
    for row in range(len(gameBoard)):
        rowOut = str("{0:0=2d}".format(row))+"|"
        for char in gameBoard[row]: rowOut += char
        print(rowOut)

def getUserAction(height:int, width:int):
    
    symbol = input("Please enter a symbol:\t")
    row    = input(f"Please select a row [0,{width}]:\t")
    column = input(f"Please select a col [0,{height}]:\t")

    return [symbol,row,column]

def fill(gameBoard:list, toReplace:str, symbol:str, row:int, column:int):
    
    if toReplace == symbol: return
    
    return
    
def main():
    #print(readLevel(1))
    displayBoard(readLevel(5))

main()