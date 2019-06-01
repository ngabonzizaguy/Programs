# to use  function from python 3 in python 2
from __future__ import print_function




#======================================================================================================================


# from IPython.display import clear_output
# # tic tac toe practice

# def display_board(board):
#     clear_output()
#     print('  -----------')
#     print('   '+board[7]+' | ' +board[8]+' | ' +board[9])
#     print('  ---|---|--- ')
#     print('   '+board[4]+' | '+board[5]+' | '+board[6])
#     print('  ---|---|--- ')
#     print('   '+board[1]+' | '+board[2]+' | '+board[3])
#     print('  -----------\n')

# def player_input():
#     marker = ''    
#     while not (marker == 'X' or marker == 'O'):
#         marker = input('player: which mark will you use. X or O ?: ').upper()
#     if marker == 'X':
#         return ('X','O')
#     else:
#         return ('O','X')

# def place_marker(board,marker,position):
#     #function to place a marker to the desired position on the numberboard pad
#     board[position] = marker

# def win_check(board,mark):
#     return ((board[7] == mark and board[8] == mark and board[9] == mark) or
#             (board[4] == mark and board[5] == mark and board[6] == mark) or
#             (board[1] == mark and board[2] == mark and board[3] == mark) or
#             (board[7] == mark and board[4] == mark and board[1] == mark) or
#             (board[8] == mark and board[5] == mark and board[2] == mark) or
#             (board[9] == mark and board[6] == mark and board[3] == mark) or
#             (board[7] == mark and board[5] == mark and board[3] == mark) or
#             (board[9] == mark and board[5] == mark and board[1] == mark))

# import random
# def choose_first():
#     if random.randint(0,1) == 0:
#        return 'Player 1'
#     else:
#        return 'Player 2'

# # RECHECK
# def space_check(board, position):
#     return board[position] == ' '

# # RECHECK
# def full_board_check(board):
#     for numberPosition in range(1,10):
#         if space_check(board,numberPosition):
#             return False
#         return True

# # RECHECK
# def player_choice(board):
#     position = ' '
#     while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
#         position = input('Choose your next move (1-9): ')
#     return int(position)

# def replay():
#     return input('Do you want to play again ?, Yes or No: ').lower().startswith('y')


# # START GAME
# print('\nWelcome to the Tic-Tac-Toe game.')
# print('*******************************\n')

# while True:
#     theBoard = [' ']*10
#     player1_marker,player2_marker = player_input()
#     turn = choose_first()
#     print(turn + ' will go first')

#     game_on = True

# while game_on:
#     if turn == 'Player 1':
#         display_board(theBoard)
#         position = player_choice(theBoard)
#         place_marker(theBoard,player1_marker,position)

#         if win_check(theBoard,player1_marker):
#             display_board(theBoard)
#             print('Congratulations, player 1 has won the game..!!')
#             game_on = False
#         else:
#             if full_board_check(theBoard):
#                 display_board(theBoard)
#                 print('The game is a draw !!')
#                 break
#             else:
#                 turn = 'Player 2'
#     else:
#         display_board(theBoard)
#         position = player_choice(theBoard)
#         place_marker(theBoard,player2_marker,position)

#         if win_check(theBoard,player2_marker):
#             display_board(theBoard)
#             print('Congratulations, player 2 has won the game..!!')
#             game_on = False
#         else:
#             turn = 'Player 1'
#         if not replay():
#             break
#======================================================================================================================







#----------------------------------------------------------------------------------------------------------------------
# GUI python codes:
# =================

# import sys
# from PyQt5 import QtWidgets


# def window():
#     app = QtWidgets.QApplication(sys.argv)
#     w = QtWidgets.QWidget()
#     w.setWindowTitle('FUTURE arrived')
#     w.show()
#     sys.exit(app.exec_())

# window()

#----------------------------------------------------------------------------------------------------------------------

#======================================================================================================================











#======================================================================================================================

# class Cylinder(object):
    
#     def __init__(self,height=1,radius=1):
#         self.height = height
#         self.radius = radius
    
#     def volume(self):
#         return self.height * (3.14) * (self.height)**2 
    
#     def surface_area(self):
#         top = (3.14) * (self.radius)**2
#         return 2*top + 2 * 3.14 * self.radius * self.height

#======================================================================================================================


# class Line(object):
    
#     m_slope = 0
    
#     def __init__(self,coor1,coor2):
#         self.coor1 = coor1
#         self.coor2 = coor2
        
#     def distance(self):
#         from math import sqrt
#         return sqrt((self.coor1[0]-self.coor2[0])**2 + (self.coor1[1]-self.coor2[1])**2)
    
#     def slope(self):
#         Line.m_slope = (self.coor2[1]-self.coor1[1]) / (self.coor2[0]-self.coor1[0])
#         return Line.m_slope
    
    
# coordinate1 = (3,2)
# coordinate2 = (8,10)
# l = Line(coordinate1,coordinate2)
# l.distance()
# l.slope()

# """
# from lecturer
# -------------

# class Line(object):
#      def __init__(self,coor1,coor2):
#          self.coor1 = coor1
#          self.coor2 = coor2
        
#      def distance(self):
#          x1,y1 = self.coor1
#          x2,y2 = self.coor2
#          return ((x2-x1)**2 + (y2-y1)**2)**0.5
      
#      def slope(self):
#          x1,y1 = self.coor1
#          x2,y2 = self.coor2
#          return float((y2-y1)) / (x2-x1)
# """

# ASSIGNMENTS II:
#===============

# 1. function that computes the volume of a sphere given its radius.

# def vol(rad):
#     return (4.0/3)*(3.14)*(rad**3)

# value = 'please input the volume of a sphere: '
# volume = vol(input(value))
# print('the volume of the sphere is now',volume)


#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 2. function to check whether a number is in a given range(inclusive high and low)

# def ran_check(num,low,high):
#     val_range = range(low,high)
#     if num in val_range:
#         print(num in val_range) # using boolean
#         print('in range')
#     else:
#         print(num in val_range) # using boolean
#         print('not in range')
        
# number = input('Enter a number: ')
# val1 = 1
# val2 = 10
# print(ran_check(int(number),val1,val2))
 

# ALTERNATE LOGIC(from lecturer):
#==============================

# def ran_check(num, low, high):
#     #check if num is between low and high (including low and high)
#     if num in range(low, high):
#         print('%s is in the range' %str(num))
#     else:
#         print('The number is outside the range.')

# number = input('Enter a number: ')
# val1 = 1
# val2 = 10
# print(ran_check(int(number),val1,val2))

# FOR RETURNING A BOOLEAN
# =======================

# def ran_check(num, low, high):
#     return num in range(low,high)

# print(ran_check(3,1,10))

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 3. a function that accepts a string and calculates the number of uppercase letters and lowercase letters

# SOLUTION FROM THE LECTURER
# ==========================

# def string__up_lo(string_sentence):
#     dict_var = {'upper':0,'lower':0}
#     for word in string_sentence:
#         if word.isupper():
#             dict_var['upper'] += 1
#         elif word.islower():
#             dict_var['lower'] += 1
#         else:
#             pass
#     print('Original string: ',string_sentence)
#     print('No. of uppercase characters: ',dict_var['upper'])
#     print('No. of lowercase characters: ',dict_var['lower'])


# st = 'Hello Mr. Rogers, how is this fine Tuesday ?'
# print (string__up_lo(st))


#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 4. function that takes a list and returns a new list of unique items from the first given list.

# def unique_list(lst):
#     lst_check = set(lst)
#     return list(lst_check)

# list_items = input('Please enter a list of items separated by commas: ')
# func_call = unique_list(list_items)
# print(func_call)


# ALTERNATE clean LOGIC(from lecturer):
#======================================   

# def unique_list(l):
#     x = []
#     for a in l:
#         if a not in x:
#             x.append(a)
#     return x

# print(unique_list([1,1,1,1,2,2,2,4,3,4,4,5,6]))

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 5. function that multiplies all the numbers in a list

# SOLUTION FROM THE LECTURE
# =========================

# def list_multiply(numbers):
#     total = numbers[0]
#     for x in numbers:
#         total *= x
#         return total

# list_multiply([1,2,3,-4])

# from lecturer not working

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 6. function that checks whether a given string is a palindrome or not.

# def palindrome(pal_string):
#     pal_string = pal_string.split()
#     for word in pal_string:
#         if word == word[::-1]:
#             print('word is palindrome, therefore it is:',word is word)
#             continue
#         else:
#             print('word is not palindrome, therefore it is:',word is not word)


# string_val = 'helleh madam nursesrun nurses run'
# func_pal = palindrome(string_val)
# print(func_pal)

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 7. 


#----------------------------------------------------------------------------------------------------------------------


#======================================================================================================================











#======================================================================================================================


# FUNCTION examples:
#-------------------

# function test example
# function to ask for user's full names and convert the first letter of the names in uppercase

# def username_uppercase(name):
#     """
#     INPUT: input all user's names
#     OUTPUT: convert the given name's first letter to uppercase

#     """
#     name = input('Enter your name please: ')
#     spliter = name.split()
#     for firstletter in spliter:
#         counter = 0
#         counter = counter + 1
#         indexer = 0
#         if firstletter[counter][indexer] != firstletter[counter][indexer].upper():
#             first_index = firstletter[indexer][indexer].upper()
#             print(first_index)
#             continue
#         else:
#             print(' ')

# arg_func = None
# username_uppercase(arg_func)
        
#----------------------------------------------------------------------------------------------------------------------

#======================================================================================================================











#======================================================================================================================

#ASSIGNEMENTS I:
#===============

#----------------------------------------------------------------------------------------------------------------------

# 1. use for, split(), and if to create a statement that will print out letters that start with 's'.

# st = 'print only the words that start with s in this sentence'
# list_split = st.split()

# for word in list_split:
#     if word[0] == 's':  
#         print(word)
          
#     else:
#         continue
        

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 2. using the range() function, print all numbers from 1-10 that are visible by 2

# rangenumber = range(1,11)
# check_test = [value for value in rangenumber if value%2==0]
# print(check_test)


#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 3. using the range() function, print all numbers from 1-50 that are visible by 3

# rangenumber = range(1,51)
# check_test = [value for value in rangenumber if value%3==0]
# print(check_test)


#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 4. use list comprehension to create a list of the first letters of every word in the string.

# st = 'create a list of the first letters of every word in this string'
# spliter = st.split()

# for word in spliter:
#     count = 0
#     singleletter = word[count]
#     count = count + 1
#     if singleletter:
#         lister = list(singleletter)
#         print(lister)
#     elif len(singleletter) <= 1 and len(singleletter) == ' ':
#         continue
#     else:
#         break


# ALTERNATIVE SIMPLE ONE
#[word[0] for word in st.split()]

#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 5. a program that prints integers from 1-100, 
# and for multiples of 3 print 'Fizz' instead of the number
#and for multiples of 5 print 'Buzz'
#and for numbers which are both multiples of 3 and 5 print'FizzBuzz'
#hhh 1hr also

# val_range = range(0,101)

# for val in val_range:
# 	a = val%3
# 	b = val%5

# 	if b == 0 and a == 0:
# 		print('3&5-FizzBuzz')
# 	elif a == 0:
# 		print('3-Fizz') 
# 	elif b == 0:
# 		print('5-Buzz')
# 	elif a != 0:
# 		continue
# 	elif b != 0:
# 		continue
# 	else:
# 		break
	
		
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------

# 6. checking for a word that has a length of an even number(:)), it had me, 3 hours,hhh

# st = 'print every word that has an even number in the sentence'
# vl = st.split()
# holder = vl
# for word in holder:
# 	if len(word)%2 == 0:
# 		print('even')
# 	else:
# 		print('odd')


#----------------------------------------------------------------------------------------------------------------------

#======================================================================================================================
