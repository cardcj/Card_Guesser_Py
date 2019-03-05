# This is the entire deck of cards that will be used in the trick
deck = [
    "Ace of Spades", "Ace of Hearts", "2 of Diamonds", "3 of Clubs",
    "4 of Spades", "5 of Hearts", "6 of Diamonds", "7 of Clubs",
    "8 of Spades", "9 of Hearts", "10 of Diamonds", "Jack of Clubs",
    "Queen of Spades", "King of Hearts", "Ace of Diamonds", "Ace of Clubs",
    "2 of Spades", "3 of Hearts", "4 of Diamonds", "5 of Clubs",
    "6 of Spades"
    ]

def get_usr_pile():
    # While loop to check whether the user enters valid input
    while True:
        usr_in = input("Which pile is your chosen card in? ")
        if 0 < int(usr_in) < 4:
            # This value is used to make sure that the user's pile is added to
            # the reformed deck between the other two piles
            return(("pile_{0}").format(usr_in))
            break
        else:
            # If the user doesn't enter 1, 2 or 3
            print("Please enter either 1, 2 or 3")
