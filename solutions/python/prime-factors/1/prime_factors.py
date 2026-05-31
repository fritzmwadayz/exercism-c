def factors(value):
    divisors = []
    divisor = 2

    while value != 1:
        if value % divisor == 0:
            divisors.append(divisor)
            value /= divisor
        else:
            divisor += 1

    return divisors
