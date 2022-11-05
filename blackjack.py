import random
import time

values = {"2":2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'King':10, 'Queen':10, 'Jack':10, 'Ace':11}
suits = ['Diamonds', 'Spades', 'Hearts', 'Clubs']

# assign cards for the hand of player:
def add_player_hand(hand, deck, n):
    for _ in range(n):
        chosen_card = random.choice(deck)
        hand.append(chosen_card)
        deck.remove(chosen_card)
    return chosen_card

# assign cards for the dealer:
def add_dealer_hand(hand, deck, n):
    for _ in range(n):
        chosen_card = random.choice(deck)
        hand.append(chosen_card)
        deck.remove(chosen_card) # removes card from deck
    return chosen_card

class Game:
    def __init__(self, values, suits):
        self.values = values
        self.suits = suits
        self.deck = list(values.keys()) * 4 # list of the whole deck (no suits assigned yet)
    
    def start_game(self):
        # shuffle the cards
        random.shuffle(self.deck)
        # initialize hand
        self.player_hand = []
        self.dealer_hand = []

        self.player_hand_total = 0
        self.dealer_hand_total = 0

        add_player_hand(self.player_hand, self.deck, 2)
        add_dealer_hand(self.dealer_hand, self.deck, 2)

        print("--------------------------------")
        print("Your hand:", ", ".join(self.player_hand))
        print("Dealer's hand:", self.dealer_hand[0]) # hidden card in dealer_hand[1]

        for i in range(len(self.player_hand)):
            if self.player_hand[i] == "Ace":
                self.player_hand_total += int(input("You have an Ace, choose it's value (11 or 1):"))
            else:
                self.player_hand_total += self.values[self.player_hand[i]]

        if self.dealer_hand[0] == "Ace":
            self.dealer_hand_total += 11
        else:
            self.dealer_hand_total += self.values[self.dealer_hand[0]]

        print(self.player_hand_total)
        print(self.dealer_hand_total)

        time.sleep(1)

        while 21 > self.player_hand_total:
            print("Hit (h) or Stand (s)?")
            choice2 = input()
        
            time.sleep(2)

            if choice2 == "h":
                ran_card = add_player_hand(self.player_hand, self.deck, 1)
                if ran_card == "Ace":
                    self.player_hand_total += int(input("You got an Ace, choose it's value (11 or 1):"))

                    print("--------------------------------")
                    print("Your hand:", ", ".join(self.player_hand))
                    print("Dealer's hand:", str(self.dealer_hand[0]))

                    print(self.player_hand_total)
                    print(self.dealer_hand_total)

                    if self.player_hand_total > 21:
                        break
                    else:
                        continue
                else:
                    self.player_hand_total += self.values[ran_card]

                    print("--------------------------------")
                    print("Your hand:", ", ".join(self.player_hand))
                    print("Dealer's hand:", str(self.dealer_hand[0]))

                    print(self.player_hand_total)
                    print(self.dealer_hand_total)

                    if self.player_hand_total > 21:
                        break
                    else:
                        continue

            else:
                break

        if self.dealer_hand[1] == "Ace":
            self.dealer_hand_total += 1
        else:
            self.dealer_hand_total += self.values[self.dealer_hand[1]]

        print("--------------------------------")
        print("Your hand:", ", ".join(self.player_hand))
        print("Dealer's hand:", ", ".join(self.dealer_hand))

        print(self.player_hand_total)
        print(self.dealer_hand_total)

        time.sleep(2)

        while self.dealer_hand_total < 17:
            dealer_card = add_dealer_hand(self.dealer_hand, self.deck, 1)

            if dealer_card == "Ace":
                self.dealer_hand_total += 1
            else:
                self.dealer_hand_total += self.values[dealer_card]

            print("--------------------------------")
            print("Your hand:", ", ".join(self.player_hand))
            print("Dealer's hand:", ", ".join(self.dealer_hand))

            print(self.player_hand_total)
            print(self.dealer_hand_total)

            time.sleep(1)
            
        if self.player_hand_total > self.dealer_hand_total and self.player_hand_total == 21:
            print("You win!")
        elif self.player_hand_total > self.dealer_hand_total and self.player_hand_total < 21:
            print("You win!")
        elif self.player_hand_total < self.dealer_hand_total and self.dealer_hand_total > 21:
            print("You win!")
        elif self.player_hand_total < self.dealer_hand_total and self.dealer_hand_total < 21:
            print("Bot wins!")
        elif self.player_hand_total == 21 and self.dealer_hand_total == 21:
            print("It's a tie!")
        elif self.player_hand_total == self.dealer_hand_total:
            print("It's a tie!")
        else:
            print("Bot wins!")

g = Game(values, suits)
g.start_game()