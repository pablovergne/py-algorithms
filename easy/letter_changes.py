# -*- coding: utf8 -*-
"""
Using the Python language, have the function LetterChanges(str) take the str parameter being passed and
modify it using the following algorithm. Replace every letter in the string with the letter following it in the
alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u)
and finally return this modified string.
"""


def letter_changes(text):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    vowels = list('aeiou')

    def next_letter(l):
        if l not in alphabet:
            return l
        else:
            return alphabet[(alphabet.index(l) + 1) % len(alphabet)]

    def upper_vowel(l):
        if l in vowels:
            return l.upper()
        return l

    l_text = list(text.lower())
    l_text = map(next_letter, l_text)
    l_text = map(upper_vowel, l_text)

    return ''.join(l_text)

print(letter_changes(raw_input()))
