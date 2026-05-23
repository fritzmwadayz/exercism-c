def leap_year(year):
    if year%4 == 0 and year%100 == 0:
        return True if year%400 == 0 else False
    
    return True if year%4 == 0 else False
