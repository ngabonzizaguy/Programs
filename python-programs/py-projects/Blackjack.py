

from __future__ import print_function
from colored import fg, bg, attr

#colors
color_magenta = fg('magenta')
color_red = fg('red')
color_yellow = fg('yellow')
color_green = fg(49)
color_light_magenta = fg(13)
color_light_cyan = fg(14)

class Deck_Ops:
    HighcardInit = {}
    Cash = 0
    betCash = 20
    remained_Cash = 0
    def __init__(self, HighCards,LowCards,hcvalues):
        self.HighCards = HighCards
        self.LowCards = LowCards
        self.hcvalues = hcvalues
    def cardAssigner(self):
        Deck_Ops.HighcardInit = {key:val for ky,val in zip(self.HighCards,self.hcvalues)}
    # def Cards_layout(self):
    #     print('\n',f'{fg(15)}''Highcards:')
    #     for key, val in Deck_Ops.HighcardInit.items():
    #         print(f'{color_red}'f'{key}','->',f'{color_light_magenta}'f'{val}')
    #     print('Lowcards:')
    #     for i in range(2,10):
    #         print('['f'{i}'']','\n')
    def CardShuffler(self):
        import random 
        from random import shuffle
        self.LowCards.extend(self.hcvalues)
        return random.choices(self.LowCards,k=2)
    # def ShuffledCards_sum(self):
    #     return sum(Deck_Ops.CardShuffler(self))
    
    def CashAmount(self):
        while not(Deck_Ops.Cash>=Deck_Ops.betCash):
            try:
                Deck_Ops.Cash = int(input('Cash: $'))
            except(ValueError):
                print('[--Invalid Literal--]')
                
    def BetAmount(self):
        while not(Deck_Ops.betCash > 20) or (Deck_Ops.betCash > Deck_Ops.Cash):
            try:
                Deck_Ops.betCash = int(input('Bet: $'))
            except(ValueError):
                print('[--Invalid Literal--]')
    
#layout class might go here
class PromptsLayout:
    def firstSectionchoices(self):
        print(f'{color_light_cyan}''\nmake a choice:')
        print('-------------')
        print('1.Deal\n0.Quit\n')
    def secondSectionchoices(self):
        print('\n1.Hit\n2.Stand\n0.Surrender\n')


class Game_ops(Deck_Ops):
    player_choice_one = None
    player_second_choice = None
    Dealer_cash = 100
    def playersChoice_one(self):
        while not(Game_ops.player_choice_one == 1 or 0):
            try:
                Game_ops.player_choice_one = int(input('>>>>: '))
            except:
                print('[-Invalid Literal--]')
    def player_choice_two(self):
        while not (Game_ops.player_second_choice == 1 or 2 or 0):
            try: 
                Game_ops.player_second_choice = int(input('>>>>: '))
            except:
                print('[--Invalid Literal--]')
    def DealerRand(self):
        self.CardShuffler()
        

print('\n'f'{fg(255)}Welcome to the 'f'{fg(200)}''BLACKJACK_21 'f'{fg(255)}''Game')
print('----------------------------------\n')

#Game Setup
while True:
    #Game_class Definitions
    highcard = [letter for letter in 'akjq'.upper()]
    lowcard = [i for i in range(2,10)]
    highcard_values = [10]*4
    #Deck_class
    Deck = Deck_Ops(highcard,lowcard, highcard_values)
    shuffledCards_holder = Deck.CardShuffler()
    #Layout_class
    promptMsg = PromptsLayout()
    #Game_ops_class
    Gamewheels = Game_ops(highcard,lowcard,highcard_values)
    game_on = True
    break

print(f'{fg(255)}Please, Enter your account balance and bet')
Deck.CashAmount()
Deck.BetAmount()

promptMsg.firstSectionchoices()
Gamewheels.playersChoice_one()
# promptMsg.secondSectionchoices()

# #GAME BEGINS
while game_on:
#     #first Game Choices
#     # make a choice:
#     # 1.Deal
#     # 0.Qut
    if Gamewheels.player_choice_one == 1:
        print('\nP:>>>',Gamewheels.player_choice_one)
        print(shuffledCards_holder,' = ',sum(shuffledCards_holder))
    elif Gamewheels.player_choice_one == 0:
        exit()
            
#     #second Game Choices
#     # 1.Hit
#     # 2.Stand
#     # 0.Surrender
#     Gamewheels.player_choice_two()
#     if Gamewheels.player_second_choice == 1:
#         print(shuffledCards_holder,' = ',sum(shuffledCards_holder))

    break














# class Bankroll:
#      min_cashAmount = 20
#      remained_Cash = 0
#      def __init__(self,playercurrentcash,bettingMoney):
#          self.playercurrentcash = playercurrentcash
#          self.bettingMoney = bettingMoney
#      def Cash(self):
#          while not(self.playercurrentcash>=Bankroll.min_cashAmount):
#              try:
#                  self.playercurrentcash = int(input('Cash: $'))
#              except (ValueError):
#                  print('[--Invalid Literal--]')
#      def Chips(self):
#          while not(self.bettingMoney>=Bankroll.min_cashAmount) or (self.bettingMoney>self.playercurrentcash):
#              print('\n[ATTENTION]\nbet can\'t exceed your $'f'{self.playercurrentcash}','or go below $'f'{Bankroll.min_cashAmount}','\n')
#              try:
#                  self.bettingMoney = int(input('Bet: $'))
#              except(ValueError):
#                  print('[--Invalid Literal--]\n')
#      def remainingCash(self):
#          Bankroll.remained_Cash = self.playercurrentcash - self.bettingMoney
#          print('Remaining Cash: $'f'{Bankroll.remained_Cash}','\n')


# class DeckOps(object):
#      def __init__(self,Hit,Deal,Stand):
#          self.hit = Hit
#          self.deal = Deal
#          self.stand = Stand

# def CardShuffler():
#     highcards = {'A': 10,'K': 10,'J': 10,'Q': 10}
#     lowcards = [2,3,4,5,6,7,8,9]
#     lowcards.extend(highcards)
#     import random
#     randomize = random.choices(lowcards,k=2)
#     return randomize

# def Replay():
#     return input('Do you wish to replay ? (Y/N): ').lower().startswith('y')



# #class definitions
# hitmove = 1
# dealmove = 2
# standmove = 0
# mincards = [2,3,4,5,6,7,8,9]
# deck = DeckOps(hitmove,dealmove,standmove)

# #function definitions
# HighCards = ['A','K','J','Q',10]

# #blackjack game startup messages
# print('\nWelcome to the Blackjack Game.(:)enjoy)')
# print('---------------------------------------\n')
# print('Enter the amount of money before placing any bet.')
# playercash = 0
# playerbet = 0
# bank = Bankroll(playercash,playerbet)
# bank.Cash()
# print(('\nCards to play').upper())
# print('-----oOo-----')
# print('HighCards:'f'{HighCards}')
# print('LowCards: 'f'{mincards}','\n')
# print('Every highcard is worth [$10] except 10 itself.\n & [A] becomes 1 if the total of your cards is 20.\n')
# print('\n.............|.......GAME_BEGINS.......|.............')
# print('1.Proceed')
# print('0.Quit\n')

# #game wheels
# choice = None
# while not(choice == 1 or 0):
#     try:
#         choice = int(input('>>>: '))
#     except (ValueError):
#         print('[--Invalid Literal--]')
#         continue
#     break

# if choice == 1:
#     bank.Chips()
# elif choice == 0:
#     print('Game Terminated..')
#     exit()
# print('\nmake a choice:\n1.Deal\n0.Quit\n')

# playerchoice = None

# while not (playerchoice == 1 or 0):
#     try:
#         playerchoice = int(input('>>>: '))
#     except ValueError:
#         print('[--Invalid Literal--]')
#         continue
#     break
# if playerchoice == 1:
#     print('cards->:',CardShuffler(),'=',sum(list(map(int, CardShuffler()))))
# elif playerchoice == 0:
#     print('Quitting game..!!')
#     exit()


