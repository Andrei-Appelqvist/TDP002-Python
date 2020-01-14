import random
from Card_D import *
from numpy import sum
import numpy as np


def get_letter(val):
    conversion = {1: "A", 2: "B", 3: "C", 4: "D", 5: "E", 6: "F", 7: "G", 8: "H", 9: "I", 10: "J", 11: "K", 12: "L",
                  13: "M", 14: "N", 15: "O", 16: "P", 17: "Q", 18: "R", 19: "S", 20: "T", 21: "U", 22: "V", 23: "W",
                  24: "X", 25: "Y", 26: "Z"}
    return conversion[val]


def solitaire_keystream(length, deck):
    keystream = ""

    while len(keystream) < length:

        #Joker A
        position = get_position(("A", "J"), deck)
        deck_length = len(deck)
        if position == deck_length:
            change_pos(("A", "J"), 1, deck)
        else:
            position += 1
            change_pos(("A", "J"), position, deck)

        #Joker B
        position = get_position(("B", "J"), deck)
        deck_length = len(deck)
        if position == deck_length:
            change_pos(("B", "J"), 3, deck)
        elif position == (deck_length-1):
            change_pos(("B", "J"), 2, deck)
        else:
            position += 2
            change_pos(("B", "J"), position, deck)

        #Dela kortleken A B C och flytta om till C B A.
        Joker_A = get_position(("A", "J"), deck)
        Joker_B = get_position(("B", "J"), deck)

        A = deck[0:Joker_A - 1]
        B = deck[Joker_A - 1:Joker_B]
        C = deck[Joker_B: len(deck)]
        deck = []
        for i in C:
            deck.append(i)
        for i in B:
            deck.append(i)
        for i in A:
            deck.append(i)


        #Flytta lika många kort från ovansidan som värdet på understa kortet.
        last_card = last_card_val(deck)  #deck[sista kortet][värde 1 (value) av kortet (suit, value)]
        if last_card == "J":
            card_count = 14
        else:
            card_count = last_card

        while card_count > 0:
            for i in deck:
                change_pos(i, len(deck) - 1, deck)
                card_count -= 1
                break

        #Räkna kort och få fram keystream.
        val_top_card = g_value(get_card(1, deck))
        if val_top_card == "J":
            key_card_value = 27
        else:
            key_card_value = g_value(get_card(val_top_card +1, deck))


        if key_card_value == "J":
            keystream = keystream
        else:
            keystream = keystream + get_letter(key_card_value)
    return keystream

def clean_message(text):
    text = text.upper()
    A_Z = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z']
    message = ""
    for t in text:
        if t in A_Z:
            message += t
    return message


def convert_letters(text):
    conversion = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                  'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                  'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                  'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                  'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                  'Z': 26}
    numbers = []
    for t in text:
        for k in conversion:
            if t == k:
                numbers.append(conversion[k])
    return numbers


def sum_msgs(message1, message2):
    sum_lst = sum([message1, message2], axis=0)
    final_lst = []
    for i in sum_lst:
        if i > 26:
            final_lst.append(i-26)
        else:
            final_lst.append(i)
    return final_lst

def subs_msgs(message1, message2):
    subs_lst = list(np.array(message1) - np.array(message2))
    final_lst = []
    for i in subs_lst:
        if i < 1:
            final_lst.append(i + 26)
        else:
            final_lst.append(i)
    return final_lst



def convert_numbers(numbers):
    conversion = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
                  'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
                  'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
                  'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
                  'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25,
                  'Z': 26}
    string = ""
    for n in numbers:
        for k in conversion:
            if n == conversion[k]:
                string += k
    return string


def solitaire_encrypt(text, deck):
    deck = create_deck()
    deck_shuffle(deck, 24)
    message = clean_message(text)
    key_stream = solitaire_keystream(len(message), deck)
    msg_num = convert_letters(message)
    key_num = convert_letters(key_stream)
    sum_msg = sum_msgs(msg_num, key_num)
    encrypt_final = convert_numbers(sum_msg)
    return encrypt_final

def solitaire_decrypt(secret_message, deck):
    deck = create_deck()
    deck_shuffle(deck, 24)
    secret_message = secret_message.upper()
    secret_message = convert_letters(secret_message)
    decrypt = solitaire_keystream(len(secret_message), deck)
    decrypt = convert_letters(decrypt)
    decrypt_final = subs_msgs(secret_message, decrypt)
    decrypt_final = convert_numbers(decrypt_final)
    return decrypt_final

