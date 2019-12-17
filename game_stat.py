class GameStat:
    
    def __init__(self,id=0,name ="",num_plays = 0 , num_wins = 0):
        self.id = id
        self.num_plays = num_plays
        self.name = name
        self.num_wins = num_wins
        
    def __str__(self):
        string = f"\n{self.name}: #plays = {self.num_plays} #wins = {self.num_wins}"
        return string

    def update_plays(self,num_plays):
        self.num_plays += num_plays
    
    def update_wins(self,num_wins):
        self.num_wins += num_wins
    