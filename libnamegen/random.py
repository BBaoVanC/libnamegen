#!/usr/bin/env python3
"""
Random Generator.

by BBaoVanC

Generates a name by using random characters!

Examples:
    KkC44zZIkJ6b
    Mw6xAKYulItJ
    qK1Kpv89fJj1

Copyright (C) 2020 BBaoVanC
"""

# Imports
import random
import libprogress


# Generation method
def gen(count=1, debug=False, length=12):
    """
    Generate names using the random method.

    Arguments:
    count -- the amount of names to generate (default 1)
    debug -- whether debug should be printed (default False)
    """
    names = list()  # prepare blank names list
    n = 1  # prepare loop counter

    while count >= n:
        name = ""  # prepare name variable
        for _ in range(length):  # for each chracter in the name
            charset = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                       "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                       "w", "x", "y", "z", "_", "0", "1", "2", "3", "4", "5",
                       "6", "7", "8", "9"]  # character set
            char = random.choice(charset)  # nosec | choose a random character
            cap = random.choice([True, False])  # nosec | choose capitalization
            if cap:  # if it should be capitalized
                char = char.capitalize()  # capitalize the letter
            name = name + str(char)  # add the character to the name
        if debug:  # if we should output debug information
            # print progress bar for generating names
            print(libprogress.genbar(curprg=n-1, maxprg=count), end="\r")
        names.append(name)  # add the name to the name list
        n = n + 1  # increase counter

    if debug:  # if we should output debug information
        # print final progress bar
        print(libprogress.genfullbar(prg=count))
    return names  # return the name list
