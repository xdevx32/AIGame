import sys

Table = [[0 for x in range(8)] for x in range(8)]
player2_move = []

def foo():
    while True:
        player1_move = [int(x) for x in raw_input().split()]
        player1_move[0] -= 1
        player1_move[1] -= 1

        #player_move[2] == 0 -> horizontal
        #player_move[2] == 1 -> vertival
        #places the opponent's move into the table
        if player1_move[2] == 0:
            Table[player1_move[0]][player1_move[1]] = 1
            Table[player1_move[0]][player1_move[1] + 1] = 1
        elif player1_move[2] == 1:
            Table[player1_move[0]][player1_move[1]] = 1
            Table[player1_move[0] + 1][player1_move[1]] = 1
#choose our move
        dummyAlg()

#places our move into the table
        if player2_move[2] == 0:
            Table[player2_move[0]][player2_move[1]] = 1
            Table[player2_move[0]][player2_move[1] + 1] = 1
        elif player2_move[2] == 1:
            Table[player2_move[0]][player2_move[1]] = 1
            Table[player2_move[0] + 1][player2_move[1]] = 1

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
def dummyAlg():
    global player2_move
    global Table
    for x in range(0, 7):
        for y in range(0, 7):
            if Table[x][y] == 0 & y+1 <= 7 & Table[x][y + 1] == 0:
                player2_move = [x, y, 0]
                return
            elif Table[x][y] == 0 & x+1 <= 7 & Table[x + 1][y] == 0:
                player2_move = [x, y, 1]
                return
    return
#hint 24 red koito ti kazah vliza da pravi horizontalen hod (is vertical = 0) oba4e realno ili nqma hod
#za pravene ili hoda koito trqbva da se pravi e vertikalen :] (Cveti)

foo()

""""""

"""
while True:
  player1_move = Table[1][1]
  print " ".join("111")
  sys.stdout.flush()
"""
