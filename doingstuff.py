#!/usr/bin/env python3

amount = ""

def calculator(x, y):
    global amount
    amount = (x + y)
    if amount > 5:
        return amount
calculator(4, 5)

def cookie_monster(x, amount,  y="cookies"):
    
    amount = calculator(4, 5)

    print(f"{x} would love to eat {amount} {y}!!!!")
cookie_monster("Cookie Monster", amount)


