from collections import Counter

some_characters = "hello there human being"
counted_char = Counter(some_characters)
# print(counted_char.most_common(5))
print(counted_char.keys(), counted_char.values())
print(counted_char['e'])
counted_char['another'] = 'some stuff'
print(counted_char)

# let's not get carried away
counted_char = dict(counted_char)
print(counted_char)

###
import random
import string
width, height = 20, 10
matrix = []

for _ in range(height):
    row = random.choices(string.ascii_lowercase, k = width)
    matrix.append(row)
print(matrix)
for r in matrix:
    print(r)

col_2 = []
for row in matrix:
    col_2.append(row[2])
print(col_2)

# or I could use a list comp

col_5 = [row[5] for row in matrix]
print(col_5)

pickme = 7
selected_col = [row[pickme] for row in matrix]

all_columns = []
for i in range(width):
    # all_columns.append([row[i] for row in matrix])
    # append keeps the list intact
    all_columns.extend([row[i] for row in matrix])
    # all_columns += [row[i] for row in matrix] # operator version
    # for row in matrix:
    #     all_columns.append(row[i])

print(all_columns)

# view the matrix again
# for r in matrix:
#     print(r)
# add a label column at the beginning
for i, r in enumerate(matrix):
    label = 'participant ' + str(i).zfill(3)
    # print(label, r)
    r.insert(0, label) # put this in at 0th

for r in matrix:
    print(r)