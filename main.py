import random
import colorama
from colorama import Fore, Style
import getch
import sys


colorama.init()  

GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

words = []
def setup():
    with open('words/en', 'r') as doc:
        for word in doc:
            word = word.replace('\n', '')
            if len(word) == 5:
                words.append(word.lower())

secret_words = ['about', 'above', 'after', 'again', 'along', 'below', 'black', 'bring', 'carry', 'could', 'early', 'every', 'first', 'found', 'great', 'group', 'hands', 'house', 'learn', 'light', 'might', 'money', 'never', 'night', 'other', 'place', 'point', 'right', 'small', 'sound', 'start', 'state', 'still', 'story', 'study', 'table', 'their', 'thing', 'think', 'three', 'today', 'under', 'until', 'water', 'where', 'which', 'while', 'woman', 'world', 'write', 'years', 'young']

secret_word = ''

def find_occurrences(secret_word, user_input, have_founded=''):
    res = {}
    secret_word = secret_word.lower()
    user_input = user_input.lower()
    for char in secret_word:
        res[char] = []
    for uind, char in enumerate(user_input):
        if secret_word.count(char) > 0:
            for ind, schar in enumerate(secret_word):
                if (schar == char and 
                    (uind, secret_word[uind]==user_input[uind]) not in res[char]
                ):
                    # print((secret_word[uind], user_input[uind]))
                    res[char].append((uind, secret_word[uind]==user_input[uind]))
    formated_res = {}
    # print(res)


    for key, value in res.items():
        if len(value) > 0:
            formated_res[key] = []

            for el in value:
                if el[1] == True:
                    formated_res[key].append((el[0], el[1], key))

                    continue
            if len(formated_res[key]) < 1: formated_res[key].append((value[0][0], value[0][1], key))
    # print(formated_res)
    final_res = []
    for key, value in formated_res.items():
        for el in value:
            final_res.append((el[0], el[1], el[2]))
    # print(final_res)

    return final_res

def game():
    
    print("\n\n\n\n\n\n\nWelcome to wordle, I hope you'll enjoy the game, so let's start!\n\n\n\n")
    secret_word = random.choice(secret_words)
    # secret_word = "Print"
    have_founded = {
        0: (RESET, ''),
        1: (RESET, ''),
        2: (RESET, ''),
        3: (RESET, ''),
        4: (RESET, '')
    }
    for i in range(5):
        user_input = ''
        while True:
            sys.stdout.write('\r' + 'Enter a word (5 characters): ' + user_input + ' ' * (5 - len(user_input)))
            sys.stdout.flush()
            char = getch.getch()
            if char == '\n' and len(user_input) != 5 and char == ' ':
                continue
            if ((char == '\r' or char == '\n') and user_input.lower() in words): 
                if user_input.lower() == secret_word.lower():
                    print('\r' + 'Enter a word (5 characters): ' + GREEN + user_input)
                    print(GREEN + "CONGRATULATIONS!!!" + RESET + " You win.")

                    sys.stdout.flush()
                    return True
                oc = find_occurrences(secret_word, user_input)
                formatted_input = ''
                for el in oc:
                    if have_founded[el[0]] != GREEN:
                        have_founded[el[0]] = (GREEN, el[2]) if el[1] == True else (YELLOW, el[2])
                for ind, char in enumerate(user_input):

                    if char.lower() != have_founded[ind][1].lower(): 
                        formatted_input += char 

                        continue

                    formatted_input += have_founded[ind][0] + char + RESET

                print('\r' + 'Enter a word (5 characters): ' + formatted_input + ' ' * (5 - len(user_input)))
                sys.stdout.flush()
                break
            elif char == '\x7f': 
                if len(user_input) > 0:
                    user_input = user_input[:-1]  
            elif len(user_input) < 5 and char in alphabet:
                if(len(user_input) == 0): char = char.upper()
                user_input += char
    return False

def main():
    g = game()
    user_input = ''
    while True:
        if g == True:
            sys.stdout.write('\r'+"Do you want to play another game?(y,n) "+user_input)
        else:    
            sys.stdout.write('\r'+"Bro, you're suck at this game, why are you keep playing? Just give up and go kill yourself. Or maybe you wanna play again?(y/n) "+user_input)


        char = getch.getch()

        if (char == '\n' and len(user_input) != 1 or char==' '):
            continue
        if char == '\r' or char == '\n': 
            if user_input == 'n':
                return
            elif user_input == 'y':
                user_input = ''
                g = game()

        if char == '\x7f': 
            user_input = ''
        elif len(user_input) < 1 and char in ['y', 'n']:
            user_input = char 
        sys.stdout.flush()
        



if __name__ == '__main__':
    setup()
    main()