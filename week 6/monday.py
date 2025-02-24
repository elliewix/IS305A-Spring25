# while loops
# while (some boolean)
text = "here's Xsome stuff"

# a defininte loop in a while loop

i = 0
while i < len(text):
    print(text[i])
    i += 1

for c in text:
    print(c)

## using a signal value

text = "here's Xsome stuff"
i = 0
found = False
while i < len(text):
    character = text[i]
    if character == "X":
        found = True
    i += 1
    # print(found, i)

i = 0
found = False

while (not found) and (i < len(text)):
    character = text[i]
    if character == "X":
        found = True
    else:
        i += 1
    print(character, i)

# alt
i = 0
searching = True

while searching:
    character = text[i]
    if character == "X": # found the thing
        searching = False # no longer searching
    else:
        i += 1
print("x was found on", i)

### see x, backtrack by 3 but only once

i = 0
backtracked_before = False
while i < len(text):
    character = text[i]
    print(character)
    if character == "X" and (not backtracked_before):
        i -= 3
        backtracked_before = True
    else:
        i += 1

## what about simulations?

## randomly generate sums that go up to 20
# and stop once we've got there

import random
random.seed(20)
total = 0
iteration_count = 0

while total <= 20:
    rand = random.randint(0,5)
    total += rand
    iteration_count += 1
#     print(total)
#
# print(total / iteration_count)
# print(iteration_count)

iteration_data = []

for _ in range(10000):
    total = 0
    iteration_count = 0

    while total <= 20:
        rand = random.randint(0, 5)
        total += rand
        iteration_count += 1
        # print(total)

    iteration_data.append(iteration_count)

print(sum(iteration_data) / 10000)