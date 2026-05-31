def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")

    if length < 0:
        raise ValueError("slice length cannot be negative")

    if len(series) == 0:
        raise ValueError("series cannot be empty")

    if len(series) < length:
        raise ValueError("slice length cannot be greater than series length")

    result = []
    start = 0
    while start + length <= len(series):
        result.append(series[start:start + length])
        start += 1
    return result
