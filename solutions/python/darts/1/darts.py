def score(x, y):
    
    mark = x*x + y*y

    if mark > 100:
        return 0

    if mark > 25:
        return 1

    if mark > 1:
        return 5

    return 10
