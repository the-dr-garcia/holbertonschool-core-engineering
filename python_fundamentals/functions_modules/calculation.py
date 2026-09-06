#!/usr/bin/env python3
"""Print results of arithmetic operations."""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    print("{}\n{}\n{}\n{}".format(add(a, b), sub(a, b),
                                   mul(a, b), div(a, b)))
