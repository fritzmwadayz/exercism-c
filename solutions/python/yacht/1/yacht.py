from collections import Counter

# Score categories.
# Change the values as you see fit.
YACHT = 0 #all 5 die showing same face
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7 #sum, takes a combinations of 3 of one number and 2 of another
FOUR_OF_A_KIND = 8#sum of 4 dice, combo of at least 4 die with same face
LITTLE_STRAIGHT = 9 #1-2-3-4-5 ret 30
BIG_STRAIGHT = 10 #2-3-4-5-6 ret 30
CHOICE = 11 #sum, any combo


def score(dice, category):
    counts = Counter(dice)
    
    if category in (ONES, TWOS, THREES, FOURS, FIVES, SIXES):
        return counts.get(category, 0) * category
    
    if category == CHOICE:
        return sum(dice)
    
    if category == YACHT:
        return 50 if len(set(dice)) == 1 else 0
    
    if category == FULL_HOUSE:
        if sorted(counts.values()) == [2, 3]:
            return sum(dice)
        return 0
    
    if category == FOUR_OF_A_KIND:
        for face, count in counts.items():
            if count >= 4:
                return face * 4
        return 0
    
    if category == LITTLE_STRAIGHT:
        return 30 if sorted(dice) == [1, 2, 3, 4, 5] else 0
    
    if category == BIG_STRAIGHT:
        return 30 if sorted(dice) == [2, 3, 4, 5, 6] else 0
    
    return 0
