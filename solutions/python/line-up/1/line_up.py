def line_up(name, number):
    num = str(number)

    if num.endswith('11') or num.endswith('12') or num.endswith('13'):
        suffix = 'th'
    elif num.endswith('1'):
        suffix = 'st'
    elif num.endswith('2'):
        suffix = 'nd'
    elif num.endswith('3'):
        suffix = 'rd'
    else:
        suffix = 'th'

    return f'{name}, you are the {num}{suffix} customer we serve today. Thank you!'
