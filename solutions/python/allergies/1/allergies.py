score_map = {
    "eggs":1,
    "peanuts":2,
    "shellfish":4,
    "strawberries":8,
    "tomatoes":16,
    "chocolate":32,
    "pollen":64,
    "cats":128
}

class Allergies:

    def __init__(self, score):
        self.score = score

    def allergic_to(self, item):
        return (self.score & score_map[item]) != 0

    @property
    def lst(self):
        return [item for item in score_map if self.allergic_to(item)]
