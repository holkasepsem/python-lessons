#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Toto je Python: `Guess a number!`

TODO: Přidáme počítadlo pokusů!
"""

import random


def guess_number():
    """
    Funkce nebo také procedura.
    """

    guess_number = 0
    number = random.randint(1, 20)

    print("Ahoj, myslím si číslo od jedné do dvaceti.")
    print("Zkus si tipnout, které číslo si myslím.")
    
    while number != guess_number:
        try:
            guess_number = int(input("Zadej číslo: "))
        except ValueError:
            print("Nezadal jsi číslo, zkus to znovu!")
            continue

        if number == guess_number:
            print("Hurááá, uhodl jsi!")
            break

        elif number > guess_number:
            print("Myslel jsem si větší číslo!")

        else:
            print("Myslel jsem si menší číslo!")

if __name__ == "__main__":
    guess_number()
    