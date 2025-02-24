text = "some Xstuff whee "

# find the start position, which is X

i = 0
found = False
while not found and (i < len(text)):
    character = text[i]
    if character == "X":
        found = True
    else:
        i += 1

print("the starting point is", i)

## there are better ways to do this
print(text.find("X"))
print(text.split("X"))

# fuss with your iteration

i = 0
seen = False
while i < len(text):
    character = text[i]
    # when you see X, print it,
    # and backtrack 3 steps
    # but only do it once
    if (not seen) and character == "X":
        i -= 3
        seen = True
    else:
        i += 1
    print(character)


## generating values
import random
random.seed(2)
total = 0
num_iterations = 0
while total < 20:
    total += random.randint(0,5)
    num_iterations += 1
print(total, num_iterations)
print(total / num_iterations)

## what if we want to repeat this?

iteration_data = []

for _ in range(10000):
    total = 0
    num_iterations = 0
    while total < 20:
        total += random.randint(0,5)
        num_iterations += 1
    iteration_data.append(num_iterations)

print("took an average of", sum(iteration_data) / len(iteration_data), "loops")
print(max(iteration_data), min(iteration_data))


