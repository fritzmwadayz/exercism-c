def square_root(number):
    candidates = [num for num in range(0, number+1)]

    low = 0
    high = len(candidates)-1

    while low <= high:
        mid = (low+high)//2
        if candidates[mid]**2 == number:
            return candidates[mid]
        elif candidates[mid]**2 > number:
            high = mid-1
        else:
            low = mid+1
