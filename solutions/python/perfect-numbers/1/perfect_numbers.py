import math

def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    
    factors = get_factors(number)

    aliquot_sum = 0
    for num in factors:
        if num != number:
            aliquot_sum += num

    return 'perfect' if number == aliquot_sum else 'abundant' if number < aliquot_sum else 'deficient'

def get_factors(number):
    factors = []
    # Loop up to the square root of number
    for i in range(1, math.isqrt(number) + 1):
        if number % i == 0:
            factors.append(i)           # Add small factor
            
            if i != number // i:             
                factors.append(number // i)  # Add large factor
                
    return sorted(factors)