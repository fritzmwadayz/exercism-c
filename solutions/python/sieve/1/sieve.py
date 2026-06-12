def primes(limit):
    if limit < 2:
        return []
    numbers = [num for num in range(2, limit+1)]
    marked = set()

    for i, candidate in enumerate(numbers):
        if candidate not in marked:
            multiple = candidate * 2
            while multiple <= limit:
                marked.add(multiple)
                multiple += candidate

    return [num for num in numbers if num not in marked]
    