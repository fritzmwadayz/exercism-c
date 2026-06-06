import re

class PhoneNumber:
    def __init__(self, number):
        self.number = self.clean_number(number)
        self.area_code = self.number[0:3]

    def clean_number(self, s:str) -> str:
        if re.search(r'[a-zA-Z]', s):
            raise ValueError("letters not permitted")
        if re.search(r'[^0-9\s\.\-\(\)\+]', s):
            raise ValueError("punctuations not permitted")
        
        cleaned = re.sub(r'\D', '', s)
        
        if len(cleaned) < 10:
            raise ValueError("must not be fewer than 10 digits")
        if len(cleaned) > 11:
            raise ValueError("must not be greater than 11 digits")
        if len(cleaned) == 11 and cleaned[0] != '1':
            raise ValueError("11 digits must start with 1")
        if len(cleaned) == 11:
            cleaned = cleaned[1:]
        if cleaned[0] == '0':
            raise ValueError("area code cannot start with zero")
        if cleaned[0] == '1':
            raise ValueError("area code cannot start with one")
        if cleaned[3] == '0':
            raise ValueError("exchange code cannot start with zero")
        if cleaned[3] == '1':
            raise ValueError("exchange code cannot start with one")
        return cleaned
        
    def pretty(self):
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"