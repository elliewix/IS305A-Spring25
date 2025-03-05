# import random
# random.seed(64)
#
# numbers = random.choices(range(10), k = 25)
# print(numbers)
# # when we see a 0 we start a new group
#
# for i, current in enumerate(numbers):
#     if (i + 1) == len(numbers):
#         print(current, "done")
#     else:
#         upcoming = numbers[i + 1]
#         print(current, upcoming)
#         if upcoming == 0:
#             print("saw a zero!")

# now we can add in the collect and reset

import random
random.seed(64)

numbers = random.choices(range(10), k = 25)
print(numbers)
# when we see a 0 we start a new group
numbers.append(0)
groups = []
temp = []
for i, current in enumerate(numbers):
    temp.append(current)
    if (i + 1) == len(numbers):
        print(current, "done")
        groups.append(temp)
    else:
        upcoming = numbers[i + 1]
        print(current, upcoming)
        if upcoming == 0:
            print("saw a zero!")
            groups.append(temp)
            temp = []

print(groups)


# loop over the clusters

for g in groups:
    g.sort()
    print(g)