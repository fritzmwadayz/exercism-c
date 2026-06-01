def recite(start_verse, end_verse):
    subjects = [
        "",
        "house",
        "malt",
        "rat",
        "cat",
        "dog",
        "cow with the crumpled horn",
        "maiden all forlorn",
        "man all tattered and torn",
        "priest all shaven and shorn",
        "rooster that crowed in the morn",
        "farmer sowing his corn",
        "horse and the hound and the horn"
    ]

    actions = [
        "",
        "Jack built",
        "lay in",
        "ate",
        "killed",
        "worried",
        "tossed",
        "milked",
        "kissed",
        "married",
        "woke",
        "kept",
        "belonged to"
    ]

    def verse(n):
        if n == 1:
            return "This is the house that Jack built."
        prev = verse(n - 1)
        prev_without_intro = prev[len("This is the "):]
        return f"This is the {subjects[n]} that {actions[n]} the {prev_without_intro}"

    return [verse(i) for i in range(start_verse, end_verse + 1)]
