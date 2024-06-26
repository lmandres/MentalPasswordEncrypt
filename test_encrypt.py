import json
import random

import english_words


mappings = {}
with open("password_encrypt.json", "r") as filein:
    mappings = json.load(filein)


def get_word():
    word_set = english_words.get_english_words_set(['web2'], lower=True, alpha=True)
    return random.choice(list(word_set))

def encrypt_word(input_word):

    def get_map_index(map_char):

        map_dec_values = {
            "0": 0,
            "1": 1,
            "2": 2,
            "3": 3,
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "a": 10,
            "b": 11,
            "c": 12,
            "d": 13,
            "e": 14,
            "f": 15
        }
         
        map_index = mappings["alphanumeric"].upper().index(map_char.upper())
        map_value = mappings["alphanumbmap"][map_index]

        return map_dec_values[map_value]

    def get_map_digit(map_index):
        map_hex_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
        return mappings["digits"][(mappings["digits"].lower().index(map_hex_digits[map_index].lower()) + 1) % 10]

    plaintext = input_word.upper()
    cyphertext = ""

    for i in range(0, len(plaintext), 1):
        if i == 0:
            cyphertext += get_map_digit((get_map_index(plaintext[0]) + get_map_index(plaintext[-1])) % 10)
        else:
            cyphertext += get_map_digit((int(cyphertext[i-1], 16) + get_map_index(plaintext[i])) % 10)
    
    return cyphertext

try:

    while True:

        prompt = get_word()
        answer = input("What is the encoding for '{}'? ".format(prompt))

        if (answer == encrypt_word(prompt)):
            print("Correct!")
        else:
            print("Wrong.  Answer is: {}".format(encrypt_word(prompt)))

except KeyboardInterrupt:
    print("Exiting . . .")   
