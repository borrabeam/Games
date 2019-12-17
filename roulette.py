import random

class Roulette:
    


    def __init__(self):
        # self.odd = [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]
        # self.even = [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36]
        # self.low = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
        # self.high = [19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
        # self.all = ['0','1 ','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','even','odd','low','high']
        self.roll = 0
        self.id = 2
        self.player_bet = {'number' : [],'even' : 0,'odd' : 0, 'high': 0,'low': 0}

    def board(self):
        
        print("    | 1 | 6 | 9 | 12 | 15 | 18 | 21 | 24 | 27 | 30 | 33 | 36 |")
        print(" 0  | 2 | 5 | 8 | 11 | 14 | 17 | 20 | 23 | 26 | 29 | 32 | 35 |")
        print("    | 3 | 4 | 7 | 10 | 13 | 16 | 19 | 22 | 25 | 28 | 31 | 34 |")
        print("              | low(1-18) | even | odd | high(19-36) |")


    def bet(self): 
        while True:

            betType = input('Choose a number or even or odd or high or low (play): ')
            if betType == 'number':
                pick_num = float(input('Pick a number: '))               
                betAmount = int(input('Bet amount: '))
                self.player_bet[betType].append([pick_num,betAmount])
                print(self.player_bet)
                
            elif betType == 'play':
                break
            else:
                try:
                    self.player_bet[betType]
                    betAmount = int(input('Bet amount: '))
                    self.player_bet[betType] += betAmount
                    print(self.player_bet)

                except KeyError:
                    pass
    
    def spin(self):
        spin = random.randint(0,36)
        self.roll = spin
        print(f'Landed on: {spin}')

    def number(self,bet,number):
            if self.roll == number[0]:
                print(f'You win {self.roll}')
                number[1] *= 10
                
            else:
                number[1] = 0

    def even_odd(self,bet):
        if self.roll % 2 == 0:
            if bet == 'even':
                print('You win even')
                self.player_bet[bet] *= 2
            else:
                print('You lose even')
                self.player_bet[bet] = 0
        elif self.roll %2 != 0:
            if bet == 'odd':
                print('You win odd')
                self.player_bet[bet] *= 2
            else:
                print('You lose odd')
                self.player_bet[bet] = 0

    def high_low(self,bet):
        if self.roll <= 18:
            if bet == 'low':
                print('You win low')
                self.player_bet[bet] *= 2
            else:
                print('You lose low')
                self.player_bet[bet] = 0
        elif self.roll >= 19:
            if bet == 'high':
                print('You win high')
                self.player_bet[bet] *= 2
            else:
                print('You lose high')
                self.player_bet[bet] = 0

    def check(self):

        for bet in self.player_bet:
            if bet == 'number':
                if len(self.player_bet[bet]) > 0:
                    for number in self.player_bet[bet]:
                        self.number(bet,number)
            else:
                if self.player_bet[bet] > 0:
                    if bet == "even" or bet == "odd":
                        self.even_odd(bet)
                    else:
                        self.high_low(bet)












game = Roulette()

while True:
    game.board()
    game.bet()
    game.spin()
    game.check()
    

# while True:
#     game.board()

#     if game.result() == 'You Win!':
#         again = input('Play again[Y/N]: ')
#         if again == 'Y':      
#             game.board()
#             game.result()
#         elif again == 'N':
#             break
#         else:
#             again   = input('Play again[Y/N]: ')



# while True:

#     betType = input('Choose a number or type you want to bet on ')

#     if betType == :
"stb4v1cy"
"3615"
    