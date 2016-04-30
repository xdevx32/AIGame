#!/usr/bin/env python
import json
import urllib2
import subprocess
import sys
import urllib
import os
import signal

PLAYER1_SERVICE_URL = "https://islands-cons.herokuapp.com"
#PLAYER1_SERVICE_URL = "http://localhost:5000"

def get_player2_move(player1_move_str):
  proc.stdin.write(player1_move_str + '\n')
  return proc.stdout.readline()

def print_table(table):
  for rowId in range(1, 9):
    row = ''
    for colId in range(1, 9):
      row += str(table[rowId][colId]) + ' '
    print row
  print '----------------------'

def set_move(table, move, player_id):
  row = int(move['row'])
  col = int(move['column'])
  table[row][col] = player_id
  if int(move['is_vertical']) == 0:
    table[row][col + 1] = player_id
  else:
    table[row + 1][col] = player_id

table = [[0 for x in range(9)] for x in range(9)]
game = json.loads(json.loads(urllib2.urlopen(PLAYER1_SERVICE_URL + '/new').read()))
token = game['id']
action = game['action']

proc = subprocess.Popen(sys.argv[1:], stdout = subprocess.PIPE, stdin = subprocess.PIPE)

try:
  while True:
    player2_move = None

    if action['type'] == 'move':
      player1_move_str = str(action['row']) + ' ' + str(action['column']) + ' ' + str(action['is_vertical'])
      print 'Player1 move is: ' + player1_move_str + '\n'
      set_move(table, action, 1)
      print_table(table)

      player2_move_str = get_player2_move(player1_move_str)
      print 'Player2 move is: ' + player2_move_str

      player2_move_arr = player2_move_str.split(' ')
      player2_move = { 'row': player2_move_arr[0], 'column': player2_move_arr[1], 'is_vertical': player2_move_arr[2]}

      set_move(table, player2_move, 2)
      print_table(table)
    elif action['type'] == 'points':
      print 'The game finished!'
      print 'Player1 has ' + action['player1'] + ' points.'
      print 'Player2 has ' + action['player2'] + ' points.'
      break
    elif action['type'] == 'failure':
      print 'The game failed!'
      print action['message']
      break
    else:
      print action['type'] + 'is an unexpected action state'

    move_params = '?row=' + player2_move['row'] + '&column=' + player2_move['column'] + '&is_vertical=' + player2_move['is_vertical']
    action = json.loads(json.loads(urllib2.urlopen(PLAYER1_SERVICE_URL + '/' + token + move_params).read()))
finally:
  os.kill(proc.pid, signal.SIGTERM)
