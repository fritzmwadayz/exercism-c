def resistor_label(colors):
    COLORS = ['black','brown','red','orange','yellow','green','blue','violet','grey','white']

    tolerance = {
        'grey' : '0.05%',
        'violet' : '0.1%',
        'blue' : '0.25%',
        'green' : '0.5%',
        'brown' : '1%',
        'red' : '2%',
        'gold' : '5%',
        'silver' : '10%',
    }

    if len(colors) == 1:
        return "0 ohms"
    
    if len(colors) == 4:
        first_value = COLORS.index(colors[0])
        second_value = COLORS.index(colors[1])
        multiplier = COLORS.index(colors[2])
        tolerance_value = tolerance[colors[3]]
        value = ((first_value*10+second_value)*(10**multiplier)) 

    if len(colors) == 5:
        first_value = COLORS.index(colors[0])
        second_value = COLORS.index(colors[1])
        third_value = COLORS.index(colors[2])
        multiplier = COLORS.index(colors[3])
        tolerance_value = tolerance[colors[4]]
        value = ((first_value*100+second_value*10+third_value)*(10**multiplier))

    count = 0
    while value >= 1000:
        value /= 1000
        count += 1
    if value.is_integer():
        value = int(value)
    units = ['ohms', 'kiloohms', 'megaohms', 'gigaohms']
    return f"{value} {units[count]} ±{tolerance_value}"
    