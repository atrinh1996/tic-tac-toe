#! python3 
# TicTacToe.py - classic tic-tac-toe game
#

SPACES = list('123456789')      # TTT board keys
X, O, BLANK = 'X', 'O', ' '     # Constants for string values

# Purpose: Runs a game of Tic Tac Toe.
# arguments: none
# returns: nothing
def main():
    print('Welcome to Tic Tac Toe!')

    # get a blank board by creatng a TTT board dictionary
    gameBoard = getBlankBoard()

    # Set players, X goes first, O goes next
    currentPlayer, nextPlayer = X, O

    while True:
        # display board on screen
        print(getBoardStr(gameBoard))

        # ask player to pick a move, 1-9:
        move = None
        while not isValidSpace(gameBoard, move):
            print('What is {}\'s move? (1-9)'.format(currentPlayer))
            move = input()

        # make the move
        updateBoard(gameBoard, move, currentPlayer)

        # check if game-over: winner or a tie; break while loop if so
        if isWinner(gameBoard, currentPlayer):
            print(getBoardStr(gameBoard))
            print(currentPlayer + ' has won the game!')
            break
        elif isBoardFull(gameBoard):
            print(gameBoardStr(gameBoard))
            print('The game is a tie!')
            break

        # swap turns
        currentPlayer, nextPlayer = nextPlayer, currentPlayer

    # end-game message
    print('Thanks for playing!')
          

# Purpose: Create a new, blank TTT board.
# arguments: none
# returns: dictionary with key-values initialized to blanks
# effects: none
def getBlankBoard():
    board = {}     # board is a Python dicitonary
    for space in SPACES:
        board[space] = BLANK    # initialize all spaces to blanks

    return board

# Purpose: Returns a text-representation of board.
# arguments: a dictionary representing the board
# returns: string representation of board formatted
# effects: none
def getBoardStr(board):
    return '''
        {}|{}|{}  1 2 3
        -+-+-
        {}|{}|{}  4 5 6
        -+-+-
        {}|{}|{}  7 8 9'''.format(board['1'], board['2'], board['3'], 
                                    board['4'], board['5'], board['6'], 
                                    board['7'], board['8'], board['9'])

# Purpose: returns true if space on board is valid space number, and space is blank
# arguments: dictionary board and an int index called space
# returns: bool value. 
# effects: none
def isValidSpace(board, space):
    return space in SPACES and board[space] == BLANK

# Purpose: set the space on the board to the mark
# arguments: dictionary board, int index called space, and string/character 
#            representint the player's mark
# returns: nothing
# effect: changes the value of dictionary at space key.
def updateBoard(board, space, mark):
    board[space] = mark

# Purpose: Returns true if player is winner on TTT Board
# arguments: dictionary board, and string/charcter of player
# returns: bool value
# effects: none
def isWinner(board, player):
    b, p = board, player

    # Check for winning conditions: Across, Down, Diagonal
    return ( (b['1'] == b['2'] == b['3'] == p) or   # Top Across
             (b['4'] == b['5'] == b['6'] == p) or   # Mid Across
             (b['7'] == b['8'] == b['9'] == p) or   # Low Across
             (b['1'] == b['4'] == b['7'] == p) or   # Left Down
             (b['2'] == b['5'] == b['8'] == p) or   # Mid Down
             (b['3'] == b['6'] == b['9'] == p) or   # Right Down
             (b['1'] == b['5'] == b['9'] == p) or   # Diagonal
             (b['3'] == b['5'] == b['7'] == p) )    # Diagonal

# Purpose: returns true if every space on board is taken
# arguments: dictionary board
# returns: bool value
# effects: none.
def isBoardFull(board):
    for space in SPACES:
        if board[space] == BLANK:
            return False

    return True
    

# main program
if __name__ == '__main__':
    main()
