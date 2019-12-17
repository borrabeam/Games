from blackjack import Blackjack, run_bj
# from high_low import Highlow
# from roulette import Roulette
from player import Player




def menu():
    print(" Select your choice ")
    print("Each game use 20 coins")
    print("1. Play Blackjack")
    print("2. Play Roulette")
    print("3. Play Hi-lo")
    print("4. See your profile")
    print("5. Stop playing")
    menu_num=int(input(""))
    return menu_num


name = input("Enter your name: ")
player = Player(name)
a = menu()
while a != 5:
    if a == 1:
        blackjack = Blackjack()
        run = run_bj(blackjack)
        player.stat.num_wins += run
    a = menu()
    # elif a == 2:
    #     roulette = Roulette()
    # elif a == 3:
    #     hi-lo = Highlow()
    # elif a == 4:

    
