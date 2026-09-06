#!/usr/bin/env python3
"""Import functions from calculator_1 and print results."""
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if __name__ == "__main__":
    print(add(a, b))
    print(sub(a, b))
    print(mul(a, b))
    print(div(a, b))
