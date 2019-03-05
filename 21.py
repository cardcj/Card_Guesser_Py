# Importing the deck and the function to get the user's pile
import cards_and_functions

def deal_cards():
    # For loop used to deal the cards
    for card in range(len(cards_and_functions.deck)):
        # If statements to check if pile_1 is equal to pile_2 and pile_3
        # It adds a card to pile 1 and further iterations check other piles
        if len(pile_1) == len(pile_2) and len(pile_1) == len(pile_3):
            pile_1.append(cards_and_functions.deck[card])
        elif len(pile_2) < len(pile_1):
            pile_2.append(cards_and_functions.deck[card])
        else:
            pile_3.append(cards_and_functions.deck[card])

# Used to combine the piles into one deck again
def reform_deck(usr_pile):
    # The following statements check which pile the user's card is in and then
    # place that pile between the other two in the reformed deck
    if usr_pile == "pile_1":
        cards_and_functions.deck = pile_2
        cards_and_functions.deck.extend(pile_1)
        cards_and_functions.deck.extend(pile_3)
    elif usr_pile == "pile_2":
        cards_and_functions.deck = pile_1
        cards_and_functions.deck.extend(pile_2)
        cards_and_functions.deck.extend(pile_3)
    else:
        cards_and_functions.deck = pile_1
        cards_and_functions.deck.extend(pile_3)
        cards_and_functions.deck.extend(pile_2)
    return(cards_and_functions.deck)

# Used to make sure that the dealing and reforming of the piles happens x3
for i in range(0, 3):
    # Emptying the pile lists ready for the cards to be added to again
    pile_1 = []
    pile_2 = []
    pile_3 = []
    # Call function to deal the cards into the piles
    deal_cards()
    # Clear the deck so that there aren't duplicate cards
    cards_and_functions.deck.clear()
    # Display piles to the user
    print(pile_1)
    print(pile_2)
    print(pile_3)
    # Instruction for the user that appears the first time cards are dealt
    if i == 0:
        print("Pick a card from any of the three piles")
    # Call function to get the user's pile and store value that is returned
    usr_pile = cards_and_functions.get_usr_pile()
    # Reform the deck with the user's pile in the middle
    reform_deck(usr_pile)
    # Increment the loop to prevent infinite looping and continue to next turn
    i += 1

# Guess the user's card (the 11th card in the deck)
print(("Your card is: {0}").format(cards_and_functions.deck[10]))
