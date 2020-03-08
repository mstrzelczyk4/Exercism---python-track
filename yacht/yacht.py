"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 1
ONES = 2
TWOS = 3
THREES = 4
FOURS = 5
FIVES = 6
SIXES = 7
FULL_HOUSE = 8
FOUR_OF_A_KIND = 9
LITTLE_STRAIGHT = 10
BIG_STRAIGHT = 11
CHOICE = 12


def score(dice, category):
    dice.sort()
    if category == YACHT:
        if len(set(dice)) == 1:
            return 50
    elif category == ONES:
        return dice.count(1)
    elif category == TWOS:
        return dice.count(2) * 2
    elif category == THREES:
        return dice.count(3) * 3
    elif category == FOURS:
        return dice.count(4) * 4
    elif category == FIVES:
        return dice.count(5) * 5
    elif category == SIXES:
        return dice.count(6) * 6
    elif category == FULL_HOUSE:
        if len(set(dice)) == 2 and (dice.count(dice[0]) == 2 or dice.count(dice[0]) == 3):
            return sum(dice)
    elif category == FOUR_OF_A_KIND:
        if len(set(dice)) < 3 and dice[1] == dice[3]:
            return dice[1] * 4
    elif category == LITTLE_STRAIGHT:
        if len(set(dice)) == 5 and dice[4] == 5:
            return 30
    elif category == BIG_STRAIGHT:
        if len(set(dice)) == 5 and dice[0] == 2:
            return 30
    elif category == CHOICE:
        return sum(dice)
    return 0
