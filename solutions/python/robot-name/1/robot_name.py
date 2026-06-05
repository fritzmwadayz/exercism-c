import random, string

class Robot:
    used_names = set()
    
    def __init__(self):
        self._name = None

    @property
    def name(self):
        if self._name is None:
            self._name = self.generate_name()
        return self._name

    def reset(self):
        self._name = None

    @classmethod
    def generate_name(cls):
        while True:
            name = ''.join(random.choices(string.ascii_uppercase, k=2) +
                           random.choices(string.digits, k=3))
            if name not in cls.used_names:
                cls.used_names.add(name)
                return name
            