from game_stat import *

class Player:
    def __init__(self, name:str):
        self.name = name
        self.balance = 10
        self.stat = GameStat()
    def __str__(self):
        return f"Name: {self.name} \nBalance left: {self.balance} \nTotal wins: {self.stat.num_wins} \nTotal plays: {self.stat.num_plays}"
    def add_balance(self,balance):
        self.balance += balance
    def remove_balance(self, balance):
        self.balance -= balance
    
f = open("demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()