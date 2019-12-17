from error import Error,InvalidCardRank,InvalidCardSuit,InvalidInput
import sys
class Blackjack:
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.stay_val = 16
        self.id = 1
    
    
    def initialize_cards(self):
        deck = []
        for rank in self.ranks:
            for suit in self.suits:
                card = rank + ' ' + suit
                deck.append(card)
        return deck

    def shuffle_cards(self, deck):
        import random
        n = len(deck)
        for i in range(n):
            r = random.randrange(i, n)
            temp = deck[r]
            deck[r] = deck[i]
            deck[i] = temp

    def display_cards(self, lcards):
        display_str = ""
        for each_card in lcards:
            ltemp = each_card.split()
            if ltemp[1] == 'Clubs':
                display_str += ltemp[0] + '\u2663' + ' '
            elif ltemp[1] == 'Diamonds':
                display_str += ltemp[0] + '\u2666' + ' '
            elif ltemp[1] == 'Hearts':
                display_str += ltemp[0] + '\u2660' + ' '
            else:
                assert ltemp[1] == 'Spades', 'Spades expected'
                display_str += ltemp[0] + '\u2665' + ' '
        print(display_str)

    def draw_cards(self, deck, n):
        hand = []
        for i in range(n):
            hand.append(deck.pop())
        return hand

    def validate_hand(self, hand):
        """Return True if this hand is valid, return False, otherwise.
        """

        for each_card in hand:
            ltemp = each_card.split()
            try:
                if not (ltemp[0] in self.ranks):
                    raise InvalidCardRank
                if not (ltemp[1] in self.suits):
                    raise InvalidCardSuit
            except InvalidCardRank:
                print("Found this invalid rank", ltemp[0], "; rank must be in", self.ranks)
                return False
            except InvalidCardSuit:
                print("Found this invalid suit", ltemp[1], "; suite must be in", self.suits)
                return False
        return True

    def calculate_hand_value(self, hand):
        """Return the value of a given hand. When there are Ace rank cards in the hand, use the max value of Ace rank, which is 11 - 1 + the number of all Ace rank cards, if the resulting hand value is not greater than 21; otherwise, use the min value of Ace rank, which is the number of all Ace rank cards.

        >>> calculate_hand_value(['2 Clubs', 'Ace Spades', 'Ace Clubs', '4 Clubs'])
        18
        >>> calculate_hand_value(['Ace Diamonds', '8 Clubs'])
        19
        >>> calculate_hand_value(['Ace Diamonds', '8 Clubs', '7 Clubs'])
        16
        >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds'])
        12
        >>> calculate_hand_value(['Ace Hearts', 'Ace Diamonds', '2 Clubs', '10 Diamonds'])
        14
        >>> calculate_hand_value(['Jack Clubs', '7 Hearts', 'Queen Hearts'])
        27
        >>> calculate_hand_value(['King Hearts', 'Queen Clubs'])
        20
        >>> calculate_hand_value(['Ace Spades', 'Queen Spades'])
        21
        >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds'])
        17
        >>> calculate_hand_value(['4 Hearts', '9 Hearts', '4 Diamonds', '8 Spades'])
        25
        """

        assert type(hand) is list, 'Python list expected'
        assert self.validate_hand(hand), 'Invalid hand'
        val = 0
        num_ace = 0
        for card in hand:
            ltemp = card.split()
            if ltemp[0] in ['2', '3', '4', '5', '6', '7', '8', '9', '10']:
                val += int(ltemp[0])
            elif ltemp[0] in ['Jack', 'Queen', 'King']:
                val += 10
            else:
                assert ltemp[0] == 'Ace', 'Ace rank expected'
                num_ace += 1
        if num_ace == 0:
            return val
        else:
            if (val + num_ace - 1 + 11) > 21:
                return val + num_ace
            else:
                return val + num_ace - 1 + 11

    def check_for_Blackjack(self, hand):
        """Return True if a given hand is a Blackjack, return False, otherwise.

        >>> check_for_Blackjack(['Ace Diamonds', '8 Clubs'])
        False
        >>> check_for_Blackjack(['Ace Hearts', 'Ace Diamonds'])
        False
        >>> check_for_Blackjack(['King Hearts', 'Queen Clubs'])
        False
        >>> check_for_Blackjack(['Ace Spades', 'Queen Spades'])
        True
        """

        assert len(hand) == 2, 'Blakjack hand must contain exactly two cards.'
        if self.calculate_hand_value(hand) == 21:
            return True
        else:
            return False

    def must_draw_more(self, hand):
        """Return True if a given hand value is not enough to stay, return False, otherwise.
        
        >>> must_draw_more(['7 Clubs', '2 Clubs'])
        True
        >>> must_draw_more(['7 Clubs', '2 Clubs', '5 Hearts'])
        True
        >>> must_draw_more(['7 Clubs', '2 Clubs', '5 Hearts', '6 Diamonds'])
        False
        >>> must_draw_more(['Ace Diamonds', '8 Clubs', '7 Clubs'])
        False
        >>> must_draw_more(['Ace Hearts', 'Ace Diamonds'])
        True
        >>> must_draw_more(['Ace Hearts', 'Ace Diamonds', '2 Clubs', '10 Diamonds'])
        True
        """

        hand_val = self.calculate_hand_value(hand)
        if hand_val < self.stay_val:
            return True
        else:
            return False


def run_bj(blackjack):
    bj = blackjack
    deck = bj.initialize_cards()
    run = True
    win_count = 0

    while run == True:
        print(win_count)
        # shuffle the deck
        bj.shuffle_cards(deck)
        # draw a player hand
        player_hand = bj.draw_cards(deck, 2)

        # draw the computer hand
        computer_hand = bj.draw_cards(deck, 2)

        # display player_hand
        print("Your hand: ", end = '')
        bj.display_cards(player_hand)

        # display computer_hand
        print("Computer hand: ", end = '')
        bj.display_cards(computer_hand[1:])

        # check if decision can be made right away with Blackjack hands
        player_BJ = bj.check_for_Blackjack(player_hand)
        computer_BJ = bj.check_for_Blackjack(computer_hand)
        if player_BJ and computer_BJ:
            print("Both tie")
        elif player_BJ:
            print("Player wins")
        elif computer_BJ:
            print("Computer wins")

        if player_BJ or computer_BJ:
            print("Computer hand: ", end='')
            bj.display_cards(computer_hand)
            sys.exit()

        # player must draw more cards if hand value is below the threshold
        while (bj.must_draw_more(player_hand)):
            player_hand += bj.draw_cards(deck, 1)
            print("Your hand: ", end = '')
            bj.display_cards(player_hand)

        while True:
            try:
                more_card = input("More card? ")
                if more_card == 'Yes':
                    player_hand += bj.draw_cards(deck,1)
                    print("Your hand: ", end = '')
                    bj.display_cards(player_hand)
                elif more_card == 'No':
                    break
                else:
                    print("sai input dde i kuy")
                    continue
            except ValueError:
                print("Invalid input")


                
            
        # computer must draw more cards if hand value is below the threshold
        while (bj.must_draw_more(computer_hand)):
            computer_hand += bj.draw_cards(deck, 1)
            print("Computer hand: ", end = '')
            bj.display_cards(computer_hand[1:])

        # determine who wins or they are both tie
        player_stand = bj.calculate_hand_value(player_hand)
        computer_stand = bj.calculate_hand_value(computer_hand)

        if player_stand > 21:
            if computer_stand > 21:
                print("Both tie")
            else:
                print("Computer wins")
        else:
            if computer_stand > 21:
                print("Player wins")
                win_count += 1
            else:
                # the computer can fight back as it knows what the hand value for player is
                while computer_stand < player_stand:
                    computer_hand += bj.draw_cards(deck, 1)
                    computer_stand = bj.calculate_hand_value(computer_hand)
                    print("Computer hand adjusted: ", end = '')
                    bj.display_cards(computer_hand[1:])
                if computer_stand > 21:
                    print("Player wins")
                elif computer_stand == player_stand:
                    print("Both tie")
                else:
                    print("Computer wins")
        print("Computer hand final: ", end = '')
        bj.display_cards(computer_hand)
        play_again = input("Play a new round (Yes/No):")
        if play_again != "No" and play_again != "Yes":
            while play_again != "Yes" and play_again !="No":
                print("invalid input")
                play_again = input("Play a new round (Yes/No): ")
        if play_again == "No":
            break
    
    return win_count

blackjack = Blackjack()
run = run_bj(blackjack)

