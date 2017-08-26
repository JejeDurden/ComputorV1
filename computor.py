#!/usr/bin/python3

import sys
import argparse

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("<equation>", help="the full equation as a str (e.g: \"1 * X^0 + 2 * X^1 - 3 * X^2 = 4 * X^0\")")
    args = parser.parse_args()

def reduced_form(values):
    values['a'] -= values['x']
    values['b'] -= values['y']
    values['c'] -= values['z']
    reduced = "Reduced form: "
    if values['a'] == 0 and values['b'] == 0 and values['c'] == 0:
        reduced = reduced + '0 '
    if values['a'] != 0:
        reduced = reduced + str(values['a']) + ' * X^0 ';
    if values['b'] > 0 and values['a'] != 0:
        reduced = reduced + '+ ' + str(values['b']) + ' * X^1 ';
    elif values['b'] > 0:
        reduced = reduced + str(values['b']) + ' * X^1 ';
    elif values['b'] < 0:
        reduced = reduced + '- ' + str(values['b']) + ' * X^1 ';
    if values['c'] > 0 and (values['a'] != 0 or values['b'] != 0):
        reduced = reduced + '+ ' + str(values['b']) + ' * X^2 ';
    elif values['c'] > 0:
        reduced = reduced + str(values['b']) + ' * X^2 ';
    elif values['c'] < 0:
        reduced = reduced + '- ' + str(values['c']) + ' * X^2 ';
    print (reduced + "= 0")

def print_degree(values):
    if values['c'] != 0:
        print ("Polynomial degree: 2")
    elif values['b'] != 0:
        print ("Polynomial degree: 1")
    else:
        print ("Polynomial degree: 0")

def get_factor(equation, exponent):
    if equation.rfind(exponent) == -1:
        return (0);
    else:
        index = equation.find(exponent) - 4
        if equation[index].isdigit():
            number = equation[index]
            index -= 1
            while index >= 0:
                if equation[index].isdigit():
                    number = number + equation[index]
                else:
                    break
                index -= 1
            number = int(number[::-1])
            return (number)
        else:
            return (0)

def get_values(argv):
    values = {'a': 0, 'b': 0, 'c': 0, 'x': 0, 'y': 0, 'z': 0}
    if argv.rfind("=") == -1:
        return (-1)
    else:
        equation = argv.split("=")
    values['a'] = get_factor(equation[0], "X^0")
    values['b'] = get_factor(equation[0], "X^1")
    values['c'] = get_factor(equation[0], "X^2")
    values['x'] = get_factor(equation[1], "X^0")
    values['y'] = get_factor(equation[1], "X^1")
    values['z'] = get_factor(equation[1], "X^2")
    reduced_form(values)
    print_degree(values)
    return (values)

def main(argv):
    parse_arg(argv)
    values = get_values(argv[0])
    if values == -1:
        print ("Equation has wrong format. Use the -h option for help.")
        return
    print (values)

if __name__ == "__main__":
    main(sys.argv[1:])
