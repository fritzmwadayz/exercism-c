def leap_year(year):
    '''This function returns True if a year is a leap year and False otherwise.
    
    The function takes int year as a parameter'''
    if year%4 == 0 and year%100 == 0:
        return year%400 == 0
    
    return year%4 == 0
