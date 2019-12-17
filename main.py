from blackjack import Blackjack, run_bj
from high_low import Highlow, run_hl
from roulette import Roulette, run_rl
from player import Player


def menu():
    print("Each game use 1 coin")
    print("1. Play Blackjack")
    print("2. Play Roulette")
    print("3. Play Hi-Lo")
    print("4. See your profile")
    print("5. Stop playing")
    menu_num=int(input("Select your game: "))
    return menu_num

name = input("Enter your name: ")
player = Player(name)
a = menu()
while a != 5:
    if a == 1:
        player.remove_balance(1)
        print("Blackjack start!!!")
        print()
        blackjack = Blackjack()
        win, plays = run_bj(blackjack)
        player.stat.num_wins += win
        player.stat.num_plays += plays
    elif a == 2:
        player.remove_balance(1)
        print("Roulette start!!!")
        print()
        roulette = Roulette()
        run_rl()
    elif a == 3:
        player.remove_balance(1)
        print("Hi-Lo start!!!")
        print()
        hi_low = Highlow()
        win, plays = run_hl(hi_low)
        player.stat.num_wins += win
        player.stat.num_plays += plays
    elif a == 4:
        player.remove_balance(1)
        print("Here is your profile!!!")
        print()
        print(player.__str__())
    a = menu()
    print()
print("Bye, Goodluck next time")





