#!/usr/bin/env python3
"""
Unique Characters in a String
Write a unique_characters() function that determines if any given
string has all unique characters (i.e. no character in the string is
duplicated). If the string has all unique characters, the function
should return True. If the string does not have all unique characters,
return False.

For example, unique_characters("apple") should return False.

This challenge and variations of it were reported to have been asked
at interviews with Google. If you’ve covered the material in Pass the
Technical Interview with Python or an equivalent, you should be able to
solve this challenge. If you have trouble, try refreshing your
knowledge there first.

Note that if the function is called with an empty string (""), the
program should return an error message.
"""


def unique_characters(string_in):
    if not string_in:
        return "Empty string"

    characters = {}
    for character in string_in:
        if characters.get(character, False):
            return False
        else:
            characters[character] = True

    return True


if __name__ == '__main__':
    print(unique_characters("apple"))
