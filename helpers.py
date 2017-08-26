def reduced_form(values):
    values['a'] -= values['w']
    values['b'] -= values['x']
    values['c'] -= values['y']
    values['d'] -= values['z']
    reduced = "Reduced form: "
    if values['a'] == 0 and values['b'] == 0 and values['c'] == 0 and values['d'] == 0:
        reduced = reduced + '0 * X^0 '
    if values['a'] != 0:
        reduced = reduced + str(values['a']) + ' * X^0 ';
    if values['b'] > 0 and values['a'] != 0:
        reduced = reduced + '+ ' + str(values['b']) + ' * X^1 ';
    elif values['b'] > 0:
        reduced = reduced + str(values['b']) + ' * X^1 ';
    elif values['b'] < 0:
        reduced = reduced + '- ' + str(values['b'] * -1) + ' * X^1 ';
    if values['c'] > 0 and (values['a'] != 0 or values['b'] != 0):
        reduced = reduced + '+ ' + str(values['c']) + ' * X^2 ';
    elif values['c'] > 0:
        reduced = reduced + str(values['c']) + ' * X^2 ';
    elif values['c'] < 0:
        reduced = reduced + '- ' + str(values['c'] * -1) + ' * X^2 ';
    if values['d'] > 0 and (values['a'] != 0 or values['b'] != 0 or values['c'] != 0):
        reduced = reduced + '+ ' + str(values['d']) + ' * X^3 ';
    elif values['d'] > 0:
        reduced = reduced + str(values['d']) + ' * X^3 ';
    elif values['d'] < 0:
        reduced = reduced + '- ' + str(values['d'] * -1) + ' * X^3 ';
    print (reduced + "= 0")
    return (reduced + "= 0")

def get_factor(equation, exponent):
    if equation.rfind(exponent) == -1:
        return (0);
    else:
        index = equation.find(exponent) - 4
        sign = '+'
        if equation[index].isdigit() or equation[index] == '.':
            number = equation[index]
            index -= 1
            while index >= 0:
                if equation[index].isdigit() or equation[index] == '.':
                    number = number + equation[index]
                else:
                    if equation[index] == '-':
                        sign = '-'
                    else:
                        if equation[index - 1] == '-':
                            sign = '-'
                    break
                index -= 1
            number = float(number[::-1])
            if sign == '-':
                number *= -1
            return (number)
        else:
            return (0)
