#!/usr/bin/env python3

import random

x = 1

def rock_paper_scissors():
    global x
    
    bot_options = ["rock", "paper", "scissors"]

    human_option = input("Let's play a game. Select rock, paper, or scissors: ").lower()
    
    # None is the equivalent of null in Python
    #x = None

    bot_option = random.choice(bot_options)
    
    if human_option == bot_option:
        answer=input(f"You have tied! You selected {human_option} and the computer selected {bot_option}. Want to play again y/n? ").lower()
        if answer == "y":
            x = x + 1
            rock_paper_scissors()
        else:
            exit()
    elif human_option == "rock" and bot_option == "paper" or human_option == "paper" and bot_option == "scissors" or human_option == "scissors" and bot_option == "rock":
        answer=input(f"You have lost! You selected {human_option} and the computer selected {bot_option}. Want to play again y/n? ").lower()
        if answer == "y":
            x = x + 1
            rock_paper_scissors()
        else:
            exit()
    else:
        answer=input(f"You have won!!! Congratulations!!! You selected {human_option} and the computer selected {bot_option}. It took you {x} attempts to win.  Want to play again y/n? ").lower()
        if answer == "y":
            rock_paper_scissors()
            x = 1
        else:
            exit()
            
rock_paper_scissors()

