import random
card_rank = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
suits = []

print("""
      
*** WELCOME TO THE DECK SHUFFLER ***
       
The deck is Shuffle now!""")


def suit_create(suit):
    for rank in card_rank:
        card = (str(rank) + " " + suit)
        suits.append([card])


suit_create("Hearts")
suit_create("Spades")
suit_create("Clubs")
suit_create("Diamonds")


deck = list(suits)
random.shuffle(deck)

for card in deck:
    choose = input("""
Press Enter to Deal a new Card, or "q" to Quit
""")
    if choose == "q":
        print("*** Bye! ***")
        break
    print(card)
else:
    print("""

Oops! The deck is empty

""")
