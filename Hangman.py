from random import *
from string import *
from sys import *

# Our words
words = [
    'developer', 'yasan', 'downwithidle', 'vscode', 'pycharm', 'python', 'c',
    'kotlin', 'cpp', 'django', 'php', 'C#', 'JavaScript', 'website'
]

answer = "y"
# Wrongs Int
wrongs = 0

# Choose a random word
chosen = words[randint(0, len(words - 1))]
chosen = chosen.upper()

# Make a array that it length equals to number of letters in ourd choosen word and fill it with -
user_list = ['-'] * len(chosen)

print(chosen)

while answer == "y":
    print(user_list, end=" - - ")
    guess = input("Guess a letter: ")
    guess = guess.upper()

    if wrongs == len(chosen):
        print("You lose")
        answer = input("do you want to continue? (y/n) ")
        if answer == "n":
            print("bye bye")
            exit()
        else:
            wrongs = 0
            guess = ""

    if chosen.count(guess) == 0:
        wrongs += 1
        print("not this word! you have", len(
            chosen) - (wrongs-1), "chances left!")
    else:
        for i in range(len(chosen)):
            if guess == chosen[i]:
                user_list[i] = guess
    if user_list.count("-") == 0:
        print("  :D - You Win - Congratulations!!!")
        answer = input("do you want to continue? (y/n) ")
        if answer == "y":
            wrongs = 0
            chosen = words[randint(0, len(words) - 1)]
            chosen = chosen.upper()
            print(chosen)
            user_list = ['-'] * len(chosen)
        else:
            print("bye bye")
            exit()
