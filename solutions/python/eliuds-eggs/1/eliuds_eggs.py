def egg_count(display_value):
    value = display_value
    count = 0
    while value != 0:
        if value%2 == 1:
            count += 1
        value //= 2

    return count
        