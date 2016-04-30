#to start the game run "player2.py python demoPlayer2.py" from the command prompt
import sys

MatrixWidth = 8
MatrixHeight = 8
Matrix = [[0]*MatrixWidth for i in range(MatrixHeight)]

class Move:

    player = 1
    x = 0
    y = 0
    isHorizontal = 0

    deltaX = 0
    deltaY = 1

    def __init__(self, x, y, isHorizontal, player):
        self.x = x
        self.y = y
        self.isHoriznotal = isHorizontal
        self.player = player

        if isHorizontal:
            self.deltaX = 0
            self.deltaY = 1
        else:
            self.deltaX = 1
            self.deltaY = 0

def recordMove (move):
    global Matrix
    Matrix[move.x][move.y] = move.player
    Matrix[move.x + move.deltaX][move.y + move.deltaY] = move.player


def zmiqta_spas():
    while True:
    	#this is how you access global variables in python...
    	global Matrix,MatrixWidth,MatrixHeight

    	#[X,Y,BlockType]
    	#Horizontal block = 0, vertical block = 1
    	#this reads the input and parses it to int
        player1_move = [int(x) for x in raw_input().split()]

        #the matrix begins from [0][0] but in the game we count from [1][1] so we take the input and substract 1 from x and y
        player1_move_X = player1_move[0] - 1
        player1_move_Y = player1_move[1] - 1
        player1_move_BlockType = player1_move[2]

        Move player1_move = Move(player1_move_X,player1_move_Y,player1_move_BlockType)


        #dont forget to record the move in your matrix

        #this is a hardcoded move for player 2
        player2_move_X = 0
        player2_move_Y = 0
        player2_move_BlockType = 0

        #the matrix begins from [0][0] but in the game we count from [1][1] so we take the output and add 1 to x and y
        print str(player2_move_X + 1) + " " + str(player2_move_Y + 1) + " " + str(player2_move_BlockType)
        sys.stdout.flush()


#don't forget to call your main function in the end :P
zmiqta_spas()