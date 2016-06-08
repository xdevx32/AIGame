import sys

Table = [[0 for x in range(9)] for x in range(9)]
player2_move = []
flag = 0

def PrintMatrix():
    file = open('./debug_log_matrix.txt', 'a')
    global Table
    for x in range(0, 8):
        for y in range(0, 8):
            file.write(str(Table[x][y]) + " ")
        file.write('\n')
    file.write('\n')

def JustPrint(toPrint):
    file = open('./debug_log_matrix.txt', 'a')
    file.write(toPrint)

def Play():
    while True:
        player1_move = [int(x) for x in raw_input().split()]
        player1_move[0] -= 1
        player1_move[1] -= 1

        #player_move[2] == 0 -> horizontal
        #player_move[2] == 1 -> vertical
        #places the opponent's move into the table
        if player1_move[2] == 0:
            Table[player1_move[0]][player1_move[1]] = 1
            Table[player1_move[0]][player1_move[1] + 1] = 1
        elif player1_move[2] == 1:
            Table[player1_move[0]][player1_move[1]] = 1
            Table[player1_move[0] + 1][player1_move[1]] = 1

        PrintMatrix()
#choose our move
        whereToPlay()

#places our move into the table
        # player_move[2] == 0 -> horizontal
        # player_move[2] == 1 -> vertical
        if player2_move[2] == 0:
            Table[player2_move[0]][player2_move[1]] = 2
            Table[player2_move[0]][player2_move[1] + 1] = 2
        elif player2_move[2] == 1:
            Table[player2_move[0]][player2_move[1]] = 2
            Table[player2_move[0] + 1][player2_move[1]] = 2
        else:
            return
        PrintMatrix()

        player1_move[0] += 1
        player1_move[1] += 1
        player2_move[0] += 1
        player2_move[1] += 1
        #prints our move
        print " ".join([str(x) for x in player2_move])

       # if player2_move[1] == 7:
       #     Table[player2_move[7]]

        sys.stdout.flush()


#chooses a turn
def whereToPlay():
    # player_move[2] == 0 -> horizontal
    # player_move[2] == 1 -> vertical
    global player2_move
    global Table
    global flag
    #'''
    for x in range(0, 6):
        for y in range(0, 7):
            if Table[x][y] == 0 & y+1 <= 7 & Table[x][y + 1] == 0:
                JustPrint("Case 1"+ '\n')
                player2_move = [x, y, 0]
                JustPrint("Case 1" + " X is: " + str(x))
                JustPrint(" Y is: " + str(y) + " and the move is horizontal" + '\n')
                return
            elif Table[x][y] == 0 & x+1 <= 7 & Table[x + 1][y] == 0:
                JustPrint("Case 2" + '\n')
                player2_move = [x, y, 1]
                JustPrint("Case 2" + " X is: " + str(x))
                JustPrint(" Y is: " + str(y) + " and the move is vertical" + '\n')
                return
            elif Table[x][y] == 0 & x+1 <= 7 & Table[x][y - 1] == 0:
                JustPrint("Case 3" + '\n')
                player2_move = [x, y, 0]
                JustPrint("Case 3" + " X is: " + str(x))
                JustPrint(" Y is: " + str(y) + " and the move is horizontal" + '\n')
                return
            elif Table[x][y] == 0 & x+1 <=7 & Table[x - 1][y] == 0:
                JustPrint("Case 4" + '\n')
                player2_move = [x, y, 1]
                JustPrint("Case 4" + " X is: " + str(x))
                JustPrint(" Y is: " + str(y) + " and the move is vertical" + '\n')
                return
          #  elif Table[x][y] == 0 & x + 1 <= 7 & Table[x + 1][y + 1] == 0:
          #      player2_move = [x, y - 2, 1]
          #      JustPrint("I entered the special case !")
          #      return
            #hardcoding values
            # this places the 5 8 1 turn !

            elif Table[4][7] == 0 & Table[5][7] == 0:
                player2_move = [4 , 7, 1]
                JustPrint("I entered the special case !" + '\n')
                flag =  1
                return

    #'''
    return
#hint 24 red koito ti kazah vliza da pravi horizontalen hod (is vertical = 0) oba4e realno ili nqma hod
#za pravene ili hoda koito trqbva da se pravi e vertikalen :] (Cveti)

Play()

""""""

"""
while True:
  player1_move = Table[1][1]
  print " ".join("111")
  sys.stdout.flush()
"""
