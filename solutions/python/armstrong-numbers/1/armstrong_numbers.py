def is_armstrong_number(number):
    sum = 0

    for digit in str(number):
        sum += int(digit)**len(str(number))

    return number == sum
