# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Hello world")

"""
tic tac toe board 
[
    [-, -, -],
    [-, -, -],
    [-, -, -]
]

1. Ask user to input -> something 1-9
2. If they enter anything else, tell them to go agn
3. check if the user_input is already taken also!
4. Add it to the board
    
5. After adding to board, check if user has won: check rows, columns, diagonals
    
6. Toggle between users!

"""
userTurn = True
board = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]
turns = 0
# J
# X is True 
# O is False


# A
def printBoard():
    position = 1
    for row in board:
        for element in row:
            print(element + " <= " + str(position), end = "\t")
            position += 1
        print()

# C
def userWantsToQuit(userInput):
    if userInput == "q":
        return True
    else:
        return False

# D
def isInputOk(userInput):
    if (not userInput.isnumeric()):
        print("Please give a number instead and dont give negatives!")
        return False
    elif (int(userInput) < 1 or int(userInput) > 9):
        print("Number is out of range give 1 - 9 instead")
        return False
    else:
        return True

# F
def isTaken(position):
    coordinates = getCoordinates(position)
    row = coordinates[0]
    column = coordinates[1]
    
    if (board[row][column] == "-"):
        return False
    else:
        print("Is already taken find another spot!")
        return True
        
# G 
def getCoordinates(position):
    position = int(position)
    column = (position - 1) % 3
    row = (position - 1) // 3
    return [row, column]
    
# H
def addToBoard(position, board, userTurn):
    coordinates = getCoordinates(position)
    row = coordinates[0]
    column = coordinates[1]
    symbol = getSymbol(userTurn)
    board[row][column] = symbol
    
def getSymbol(userTurn):
    if (userTurn):
        return "X"
    else:
        return "O"
#J
def isWin(board, userTurn):
    symbol = getSymbol(userTurn)
    
    if checkRow(symbol, board): return True
    if checkCol(symbol, board): return True
    if checkDiag(symbol, board): return True
    return False

def checkRow(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot != user:
                complete_row = False
                break
        if complete_row: return True
    return False 

def checkCol(user, board):
    for col in range(3):
        complete_col = True
        for row in range(3):
            if board[row][col] != user:
                complete_col = False
                break
        if complete_col: return True
    return False

def checkDiag(user, board):
    if board[0][0] == user and board[1][1] == user and board[2][2] == user: return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user: return True
    else: return False
  
  
# B
while True:
# while turns < 9:
    printBoard()
    userInput = input("Please enter position 1 through 9 or enter \"q\" to quit: ")
    if userWantsToQuit(userInput):
        print("Thanks for playing <3")
        break
    
    if not isInputOk(userInput):
        continue
    
    if isTaken(userInput):
        continue
    
    addToBoard(userInput, board, userTurn)
    if (isWin(board, userTurn)):
        print("User " + getSymbol(userTurn) + " has won!")
        break
    # turns += 1
    # if (turns == 9): print("Tie")
    userTurn = not userTurn
    
    
    
