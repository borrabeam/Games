import random


class Highlow:
    def __init__(self):
        self.ranks =[1,2,3,4,5,6,7,8,9,10,11,12,13]
        self.deck = []
        self.draw = []
        self.id = 3

    def create_deck(self):
        for num in range(3):
            for card in self.ranks:
                self.deck.append(card)
    
    def draw_card(self):
        if len(self.deck) > 0:
            pick = random.randrange(len(self.deck)-1)
            picked = self.deck[pick]
            self.deck.remove(self.deck[pick])
            self.draw.append(picked)
            return 
        else:
            return "Out of deck"
    
    def first_draw(self):
        self.draw_card()
        return (self.draw[0])

    def compare_cards(self, prediction):
        self.draw_card()
        print(self.draw[-1])
        print(self.draw)
        if len(self.draw) > 1:
            if prediction == "high":
                if self.draw[-1] > self.draw[-2]:
                    return "You win"
                else:
                    return "You lose"
            elif prediction == "ties":
                if self.draw[-1] == self.draw[-2]:
                    return "You win"
                else:
                    return "You lose"
            elif prediction == "low":
                if self.draw[-1] < self.draw[-2]:
                    return "You win"
                else:
                    return "You lose"
        else:
            return "You must draw your card"

game = Highlow()
game.create_deck()
print(game.first_draw())



while True:
    prediction = input('high/ties/low: ')
    result = game.compare_cards(prediction)
    print(result)
    if result == 'You lose':
        com = input('Play again?[Y/N]: ')
        if com == 'N':
            break
        elif com == 'Y':
            game.create_deck()
            game.draw = []
            print(game.first_draw())
            
            

        


    


    







