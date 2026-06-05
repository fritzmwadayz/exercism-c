import re

class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        cleaned = self.card_num.replace(" ", "")

        if len(cleaned) <= 1:
            return False
            
        if not cleaned.isdigit():
            return False

        nums = [int(digit) for digit in cleaned]

        for i in range(len(nums)-2, -1, -2):
            num = nums[i]*2
            if num > 9:
                num -= 9
            nums[i] = num
        total = sum(nums)
        
        if total%10 == 0:
            return True
        return False
            