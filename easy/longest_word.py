# -*- coding: utf8 -*-
"""
Using the Python language, have the function LongestWord(sen) take the sen parameter being passed and return
the largest word in the string. If there are two or more words that are the same length, return the first word from
the string with that length. Ignore punctuation and assume sen will not be empty.
"""


def longest_word(sen):
    l_sen = str.split(sen, ' ')

    def longest(x, y):
        if len(y) > len(x):
            return y
        return x

    return reduce(longest, l_sen)

print(longest_word(raw_input()))
