def flatten(iterable):
    result = []
    for item in iterable:
        if item is None:
            continue
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)

    return result
