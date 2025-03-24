import pathlib

base = pathlib.Path("..")
print(base.absolute())
# print(list(base.glob('*')))
#
# print(list(base.rglob("*.py")))

###
# writing our own recursive functions

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n -1)

print(factorial(100))

####

base = "f-h"

new = ""
for char in base:
    if char == "f":
        new += "f-h"
    elif char == "h":
        new += "f+h"
    else:
        new += char

# print(new)

def dragon(base):
    new = ""
    for char in base:
        if char == "f":
            new += "f-h"
        elif char == "h":
            new += "f+h"
        else:
            new += char
    return new

gen2 = dragon(base)
gen3 = dragon(gen2)
gen4 = dragon(gen3)
print(gen2)
print(gen3)
print(gen4)

start = "f-h"

def make_dragon(start, gen):
    iteration = 1
    while iteration < gen:
        start = dragon(start)
        iteration += 1
    return start

print(make_dragon(start, 10))

## so let's take a look at it

import turtle

t = turtle.Turtle()
t.left(90)
d = make_dragon(start, 10)
for char in d:
    if char.isalpha():
        t.forward(10)
    elif char == "-":
        t.left(96)
    elif char == "+":
        t.right(117)
turtle.done()

# a stupid start
# def make_dragon(gen):
#     gen1 = "f-h"
#     if gen == 1:
#         return gen1
#     else:
#         gen_count = 1
#         new = ""
#         while gen_count <= gen:
#             new = dragon(gen1)
#             gen_count += 1
#         return new
