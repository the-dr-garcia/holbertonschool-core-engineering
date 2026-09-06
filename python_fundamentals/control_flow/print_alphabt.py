#!/usr/bin/env python3
result = ""
for i in range(97, 123):
    letter = chr(i)
    if letter != 'q' and letter != 'e':
        result = "{}{}".format(result, letter)
print(result)
