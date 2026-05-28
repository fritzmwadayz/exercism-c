def append(list1, list2):
    next_slot = len(list1)
    for item in list2:
        list1.insert(next_slot, item)
        next_slot += 1
    return list1


def concat(lists):
    result = []
    for item in lists:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def filter(function, list):
    result = []

    for item in list:
        if function(item):
            result.append(item)
    return result


def length(list):
    return len(list)


def map(function, list):
    result = []

    for item in list:
        result.append(function(item))
    return result


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    start = len(list)-1

    while start >= 0:
        acc = function(acc, list[start])
        start -= 1
    return acc


def reverse(list):
    start = len(list)-1
    result = []

    while start >= 0:
        result.append(list[start])
        start -= 1

    return result
