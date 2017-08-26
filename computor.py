#!/usr/bin/python3

import sys
import argparse
from helpers import get_factor, reduced_form
from maths import sq_rt

def parse_arg(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("<equation>", help="the full equation as a str (e.g: \"1 * X^0 + 2 * X^1 - 3 * X^2 = 4 * X^0\")")
    args = parser.parse_args()

def print_degree(reduced):
    degree = -1;
    for i in range(0, 4):
        exponent = "X^" + str(i)
        if reduced.rfind(exponent) != -1:
            degree = i
    if degree >= 0:
        print ("Polynomial degree:", degree)
    return (degree)

def print_discrim(values):
    discrim = values['b']**2 - 4 * values['c'] * values['a']
    if discrim > 0:
        print ("Discriminant is strictly positive, the two solutions are:")
    elif discrim == 0:
        print ("Discriminant is 0, the unique solution is:")
    else:
        print ("Discriminant is strictly negative, there is no solution")
    return (discrim)


def get_values(argv):
    values = {'a': 0, 'b': 0, 'c': 0, 'd': 0, 'w': 0, 'x': 0, 'y': 0, 'z': 0}
    if argv.rfind("=") == -1:
        return (-1)
    else:
        equation = argv.split("=")
    values['a'] = get_factor(equation[0], "X^0")
    values['b'] = get_factor(equation[0], "X^1")
    values['c'] = get_factor(equation[0], "X^2")
    values['d'] = get_factor(equation[0], "X^3")
    values['w'] = get_factor(equation[1], "X^0")
    values['x'] = get_factor(equation[1], "X^1")
    values['y'] = get_factor(equation[1], "X^2")
    values['z'] = get_factor(equation[1], "X^3")
    return (values)

def solve(degree, values):
    if degree == 2:
        discrim = print_discrim(values);
        if discrim < 0:
            return
        elif discrim == 0:
            solution = (values['b'] * -1) / (2 * values['c'])
            print (solution)
        elif discrim > 0:
            s1 = (values['b'] * -1 + sq_rt(discrim)) / (2 * values['c'] * 1.0)
            s2 = (values['b'] * -1 - sq_rt(discrim)) / (2 * values['c'] * 1.0)
            print (s1)
            print (s2)
    else:
        solution = (values['a'] * -1) / values['b']
        print (solution)

def main(argv):
    parse_arg(argv)
    values = get_values(argv[0])
    if values == -1:
        print ("Equation has wrong format. Use the -h option for help.")
        return
    reduced = reduced_form(values)
    del values['w']
    del values['x']
    del values['y']
    del values['z']
    degree = print_degree(reduced)
    if degree == 0 and reduced == "Reduced form: 0 * X^0 = 0":
        print ("There is an infinity of solutions.")
        return
    elif degree == 0:
        print ("The solution is 0.")
        return
    elif degree > 2:
        print ("The polynomial degree is stricly greater than 2, I can't solve it for now.")
        return
    del values['d']
    solve(degree, values)

if __name__ == "__main__":
    main(sys.argv[1:])
