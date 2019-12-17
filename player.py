from game_stat import *

class Player:
    def __init__(self, name:str):
        self.name = name
        self.balance = 100
        self.stat = GameStat()
    def add_balance(self,balance):
        self.balance += balance
    def remove_balance(self, balance):
        self.balance -= balance
    

    