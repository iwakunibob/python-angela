# Black Jack Game Project by Robert Laurie
import art
import random
import time

def make_deck():
    """Function makes card deck. Return deck dictionary with cards and point values"""
    fDeck = {}
    suits = ['\u2666', '\u2665',  '\u2660', '\u2663']
    ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    for suit in suits:
        for rank in ranks:
            key = rank + suit
            if rank == 'A':
                points = 11
            elif rank.isalpha():
                points = 10
            else:    
                points = int(rank)
            fDeck[key] = points
    return fDeck

def shuffle_deck(sDeck):
    """Parmameter is a deck dictionary. Returns list of shuffled cards"""
    sCards = []
    for card in sDeck:
        sCards.append(card)
    random.shuffle(sCards)

    return sCards

def deal_card(dCards):
    """Parmameters are deck dictionary and cards list. Returns one card"""
    dCard = dCards.pop(0)
    return dCard

def cards_sum(cCards, cDeck):
    """Parameters are cards list and dictionary of cards. Returns cards score"""
    sum = 0
    aces = 0
    for card in cCards: 
        sum += cDeck[card]
        if card[0] == 'A':
            aces += 1
    if sum > 21 and aces != 0:
        for _ in range(aces):
            sum -= 10
    return sum

def print_cards(pCards):
    """Parameter is cards list. Returns a string representing all cards"""
    card_string = ""
    for card in pCards:
        card_string += card + " "
    return card_string

def has_black_jack(bHand, bDeck):
    sum = cards_sum(bHand, bDeck)
    count = len(bHand)
    if sum == 21 and count == 2:
        return True
    else:
        return False

def black_jack_hand(bHand_count):
    dealer_hand = []
    gambler_hand = []
    hand_ends = False
    bHand_count += 1
    for _ in range(2):  # Loop for starting  hand of two cards each
        gambler_hand.append(deal_card(cards))
        dealer_hand.append(deal_card(cards))
        if has_black_jack(gambler_hand, deck):
            if not has_black_jack(dealer_hand, deck):
                print(f"Gambler has Black Jack {print_cards(gambler_hand)} and Wins 1.5 x bet")
            else:
                print(f"Gambler {print_cards(gambler_hand)} and Dealer {print_cards(dealer_hand)} both have Black Jack! It is a push")
            hand_ends = True
    print(f"Dealer card showing is {dealer_hand[0]}")
    while not hand_ends:  # Gambler draws more cards
        gambler_sum = cards_sum(gambler_hand, deck)
        print(f"The gambler cards are: {print_cards(gambler_hand)}which is {gambler_sum} points")
        count = len(gambler_hand)
        if gambler_sum == 21:
            print("Gambler has 21 and must hold")
            break
        elif gambler_sum > 21:
            print("Gambler is Bust and lost bet")
            hand_ends = True
        elif count == 5:
            print("Gambler has 5 Card Charlie and wins bet")
            hand_ends = True
        else:
            y_or_n = input("Would you like to draw another card (Y or N)? ").lower()
            if y_or_n == 'y':
                gambler_hand.append(deal_card(cards))
            else:
                break
    while not hand_ends:  # Dealer draws more cards
        dealer_sum = cards_sum(dealer_hand, deck)
        time.sleep(1)
        print(f"The dealer cards are: {print_cards(dealer_hand)}which is {dealer_sum} points")
        if dealer_sum < 17:
            dealer_hand.append(deal_card(cards))
        elif gambler_sum > 21:
            print("Dealer is Bust and Gambler won bet")
            hand_ends = True
        else:
            break
    if hand_ends == False:
        if gambler_sum > dealer_sum:
            print("Gambler wins bet")
        elif gambler_sum == dealer_sum:
            print("Gambler retains bet it is a push")
        else:
            print("Gambler loses bet") 
    y_or_n = input("Do you want play another hand? (Y or N)").lower()
    if y_or_n == 'y':
        black_jack_hand(bHand_count)
    else:
        print(f"Thank you for playing {bHand_count} hands of Black Jack\nGood Bye")
        return

print(art.logo)
print("Welcome to the Black Jack Game")
deck = make_deck()
cards = shuffle_deck(deck)
print(print_cards(cards))
black_jack_hand(0)
