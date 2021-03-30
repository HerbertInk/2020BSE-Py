# formulas
print("c:\\users\\hpprobook\\desktop")
# formatting strings
print(r"\ wasap\ u good?\ r #####")
name = "INK"
age = input("How old are you?:\n")
print(f"{name} is {age} years old")
print("{0} is {1} years old".format(name, age))
print("{} is {} years old".format(name, age))
# rounding
x = 23.34576
print(round(x, 3))
# using format specifiers
amt = 200114.67890
c = f"your total amount is {amt:.2}"
print(c)
d = f"your total amount is {amt:.2f}"
print(d)

import math

x = 23.34576
print("the value is", math.ceil(x))
print("the value is", math.floor(x))
# alignment
name = "Kid Ink"
m = f"{name:^50}"
n = f"{name:<70}"
print(m)
print(n)
