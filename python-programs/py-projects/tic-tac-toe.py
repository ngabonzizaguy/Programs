from __future__ import print_function
from IPython.display import clear_output

# function to display the board/
def display_board(board):
    clear_output()
    print('  -----------')
    print('   '+board[7]+' | '+board[8]+' | '+board[9])
    print('  ---|---|--- ')
    print('   '+board[4]+' | '+board[5]+' | '+board[6])
    print('  ---|---|--- ')
    print('   '+board[1]+' | '+board[2]+' | '+board[3])
    print('  -----------\n')
    # print('  |   |   ')
    # print(''+board[7]+' | '+board[8]+' | '+board[9])
    # print('-----------')
    # print('  |   |   ')
    # print(''+board[4]+' | '+board[5]+' | '+board[6])
    # print('-----------')
    # print('  |   |   ')
    # print(''+board[1]+' | '+board[2]+' | '+board[3])
    # print('-----------')
    
    
# function to prompt player to input and assign their marker as position 'X' or 'O'.
def player_input():
    marker = ''    
    while not (marker == 'X' or marker == 'O'):
        marker = input('player: which mark will you use. X or O ?: ').upper()
    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')

#function that takes, in the board list object, a marker ('X' or 'X'), and a desired position (number 1-9) and assigns it to the board
def place_marker(board, marker,position):
    board[position] = marker

#function taht takes in a board and a mark(X or O) and then checks to see if that mark has won
def win_check(board,mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or #accross the top [7-9]
    (board[4] == mark and board[5] == mark and board[6] == mark) or  # accross the middle [4-6]
    (board[1] == mark and board[2] == mark and board[3] == mark) or  # accross the bottom [1-3]
    (board[7] == mark and board[4] == mark and board[1] == mark) or # accross the vertical-first side [7-1]
    (board[8] == mark and board[5] == mark and board[2] == mark) or # accross the vertical-middle side [8-2]
    (board[9] == mark and board[6] == mark and board[3] == mark) or # accross the vertical-rightmost side [9-3]
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal [7-3]
    (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal [9-1]

#function that uses the random module to randomly decide which player goes first.
#one may want to lookup random.randint() return a string of which player went first.
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


#function that returns a boolean indicating whether a space on the board is freely available.
def space_check(board,position):
    return board[position] == ' ' 

# a function that checks if the board is full and returns a boolen value. True if full, False otherwise.
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# a function that asks for a player's next position (as a number 1-9) and the uses the function from 
#step 6 to check if its a free position. if it is, then return the position for later use
def player_choice(board):
    position = ' '

    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position = input('Choose your next position (1-9): ')
    return int(position)

# function that asks the player if they want to play again and returns a boolean True if they do want to play again.
def replay():
    return input('Do you want to play again ? Enter Yes or No: ').lower().startswith('y')

# last function to sum all functions up. by the use of while loops and the functions made to run the game..!
print('\nWelcome to the Tic-Tac-Toe game.')
print(' ********************************\n')

# while True:
while True:
  # set the game up here
  theBoard = [' ']*10
  player1_marker,player2_marker = player_input()
#same as > #player1_marker = player_input()
#same as > #player2_marker = player_input()
  turn = choose_first()
  print(turn + ' will go first')

  game_on = True

  # while game_on:
  while game_on:
      #player 1 Turn
      if turn == 'Player 1':
          display_board(theBoard)
          position = player_choice(theBoard)
          place_marker(theBoard,player1_marker,position)

          if win_check(theBoard,player1_marker):
              display_board(theBoard)
              print('Congratulations, Player 1 has won the game !!')
              game_on = False
          else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
      else:
            # player 2's turn
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print('Congratulations, Player 2 has won the game !!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is a draw')
                    break
                else:
                    turn = 'Player 1'    
          # if not replay():
            if not replay():               
              # break
                break