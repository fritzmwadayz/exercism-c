ORDINALS = [
    "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth",
    "ninth", "tenth", "eleventh", "twelfth"
]

GIFTS = [
    "a Partridge in a Pear Tree",
    "two Turtle Doves",
    "three French Hens",
    "four Calling Birds",
    "five Gold Rings",
    "six Geese-a-Laying",
    "seven Swans-a-Swimming",
    "eight Maids-a-Milking",
    "nine Ladies Dancing",
    "ten Lords-a-Leaping",
    "eleven Pipers Piping",
    "twelve Drummers Drumming",
]
def verse(day):
    gifts = []
    for i in range(day, 0, -1):
        gift = GIFTS[i-1]
        if i == 1 and day > 1:
            gift = "and a Partridge in a Pear Tree"
        gifts.append(gift)
    gifts_str = ", ".join(gifts)
    return f"On the {ORDINALS[day-1]} day of Christmas my true love gave to me: {gifts_str}."
    
def recite(start_verse, end_verse):
    return [verse(d) for d in range(start_verse, end_verse+1)]
