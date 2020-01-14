from Sol_key import *

#Joker_A = get_position(("A", "J"), deck)
#Joker_B = get_position(("B", "J"), deck)

#A = slice(1, Joker_A, deck)
#B = slice(Joker_A,Joker_B, deck)
#C = deck[Joker_B: len(deck)]
deck = create_deck()
deck_shuffle(deck, 24)
inp = input("Write a word and see if you get the same back\n")
asd = solitaire_encrypt(inp, deck)
print("Encrypted: " + asd)
print("Decrypted: "+ solitaire_decrypt(asd, deck))
