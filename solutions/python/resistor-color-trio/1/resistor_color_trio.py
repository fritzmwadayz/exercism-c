def label(colors):
    COLORS = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

    first_digit = COLORS.index(colors[0])
    second_digit = COLORS.index(colors[1])
    multiplier = COLORS.index(colors[2])
    value = (first_digit * 10 + second_digit) * (10 ** multiplier)

    count = 0

    while value > 1000:
        value //= 1000
        count += 1

    if count == 0:
        return f'{value} ohms'
    if count == 1:
        return f'{value} kiloohms'
    if count == 2:
        return f'{value} megaohms'
    if count == 3:
        return f'{value} gigaohms'
