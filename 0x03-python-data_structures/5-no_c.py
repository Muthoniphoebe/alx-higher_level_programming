#!/usr/bin/env python3
def no_c(my_string):
    new_string = my_string.translate({ord(letter): None for letter in 'cC'})
    return new_string
