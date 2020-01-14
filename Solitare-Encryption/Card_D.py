import random



def create_card(suit, val):
    card = (suit, val)
    return card

def create_deck():
    deck = []
    for suit in range(1, 3):
        for val in range(1, 14):
            deck.append(create_card(suit, val))
    deck.append(("A", "J"))
    deck.append(("B", "J"))
    return deck

def insert_card(card, position, deck):
    deck.insert(position-1, card)
    print(deck)

def deck_shuffle(deck, value):
    random.seed(value)
    random.shuffle(deck)
    return deck

def get_suit(card):
    suits = {1: "Hearts", 2: "Spades"}
    for s in suits:
        if card[0] == s:
            return suits[s]

def get_value(card):
    high_cards = {11: "Knight", 12: "Queen", 13: "King", 1: "Ace"}
    for h in high_cards:
        if card[1] == h:
            return high_cards[h]
            break
        elif card[1] < 11 and card[1] > 1:
            return card[1]
            break

def display_card(card):
    print(str(get_value(card)) + " of " + str(get_suit(card)))

def remove_card(position, deck):
    deck.pop(position - 1)
    return deck

def change_pos(card, position, deck):
    current_position = 1
    for c in deck:
        if c == card:
            remove_card(current_position, deck)
            deck.insert(position - 1, card)
            break
        else:
            current_position += 1
    return deck

def get_position(card, deck):
    position = 1
    if card not in deck:
        print("Card not in deck!")
    for d in deck:
        if d == card:
            return position
        else:
            position += 1


def get_card(position, deck):
    return deck[position -1]

def g_value(card):
    return card[1]

def last_card_val(deck):
    return deck[len(deck) - 1][1]

def slice(p1, p2, deck):
    p1 = p1 -1
    p2 = p2 - 1
    return deck[p1:p2]


#deck = create_deck()
#deck_shuffle(deck, 24)
#print(deck)