# Blackjack Game Project by Robert Laurie
import art
import random
import time

def make_deck():
    """Make card deck. Return deck dictionary with cards and point values"""
    SUITS = ['\u2666', '\u2665',  '\u2660', '\u2663']
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    deck = {}
    for suit in SUITS:
        for rank in RANKS:
            key = rank + suit
            if rank == 'A':
                points = 11
            elif rank.isalpha():
                points = 10
            else:    
                points = int(rank)
            deck[key] = points
    return deck

def shuffle_cards(deck, qty):
    """ Parmameters are a deck dictionary and quantity of decks. 
        Returns a list of shuffled cards made from multiple decks"""
    cards = []
    for _ in range(qty):
        for card in deck:
            cards.append(card)
    random.shuffle(cards)
    return cards

def deal_card(cards):
    """Parmameters is a list of cards. Returns one card"""
    card = cards.pop(0)
    return card

def cards_sum(cards, deck):
    """Parameters are cards list and dictionary of cards. Returns cards score"""
    sum = 0
    aces = 0
    for card in cards: 
        sum += deck[card]
        if card[0] == 'A':
            aces += 1
    if sum > 21 and aces != 0:
        for _ in range(aces):
            sum -= 10
    return sum

def cards_string(cards):
    """Parameter is cards list. Returns a string representing all cards"""
    string = ""
    for card in cards:
        string += card + " "
    return string

def black_jack_hand(cards, chips):
    dealer_hand = []
    gambler_hand = []
    hand_ends = False
    while True:
        bet = int(input(f"You have ${chips} in chips. What is your bet ? $"))
        if bet <= chips:
            break
        else:
            print(f"Your bet cannot excede your chips. Try again")
    for _ in range(2):  # Loop for starting  hand of two cards each
        gambler_hand.append(deal_card(cards))
        dealer_hand.append(deal_card(cards))
    print(f"Dealer card showing is {dealer_hand[0]}")
    if cards_sum(gambler_hand, deck) == 21:
        if cards_sum(dealer_hand, deck) == 21:
            print(f"Both the Gambler {cards_string(gambler_hand)} and Dealer {cards_string(dealer_hand)} have Black Jack!\nIt is a push")
        else:
            print(f"Gambler has Black Jack {cards_string(gambler_hand)} and Wins 1.5 x bet. Dealer had {cards_string(dealer_hand)}")
            chips += bet * 1.5
        hand_ends = True
    while not hand_ends:  # Gambler draws more cards
        gambler_sum = cards_sum(gambler_hand, deck)
        print(f"The gambler cards are: {cards_string(gambler_hand)}which is {gambler_sum} points")
        count = len(gambler_hand)
        if gambler_sum == 21:
            print("Gambler has 21 and must hold")
            break
        elif gambler_sum > 21:
            print("Gambler is Bust and lost bet")
            chips -= bet
            hand_ends = True
        elif count == 5:
            print("Gambler has 5 Card Charlie and wins bet")
            chips += bet
            hand_ends = True
        else:
            y_or_n = input("Would you like to draw another card (y or n)? ").lower()
            if y_or_n == 'y':
                gambler_hand.append(deal_card(cards))
            else:
                break
    while not hand_ends:  # Dealer draws more cards
        dealer_sum = cards_sum(dealer_hand, deck)
        time.sleep(0.8)
        print(f"The dealer cards are: {cards_string(dealer_hand)}which is {dealer_sum} points")
        if dealer_sum < 17:
            dealer_hand.append(deal_card(cards))
        elif dealer_sum > 21:
            print("Dealer is Bust and Gambler won bet")
            chips += bet
            hand_ends = True
        else:
            break
    if hand_ends == False:
        if gambler_sum > dealer_sum:
            print("Gambler wins bet")
            chips += bet
        elif gambler_sum == dealer_sum:
            print("Gambler retains bet it is a push")
        else:
            print("Gambler loses bet") 
            chips -= bet
    print(f"{len(cards)} cards remaining")
    y_or_n = input("Do you want play another hand (y or n)? ").lower()   
    if y_or_n == 'y':
        if len(cards) < 30:
            cards = []
            cards = shuffle_cards(deck, decks)
            print("Please wait reshuffling cards")
            time.sleep(1)
        if chips <= 0:
            print(f"You are bankrupt and need to buy more chips\nGood Bye")
            return
        else:
            black_jack_hand(cards, chips)
    else:
        print(f"Thank you for playing Blackjack\nGood Bye")
        return

print(art.logo)
print("Welcome to the Blackjack Game")
deck = make_deck()
decks = int(input("How many 52 card decks would you like to use? "))
cards = shuffle_cards(deck, decks)
print(cards_string(cards))
chips = int(input("How many chips would you like to buy ? $"))
black_jack_hand(cards, chips)
