import random
import string

# list concatenation

print([0] + [0] + [0])
print([0] * 3)

l = []
for _ in range(20):
    l.append(0)
print(l)

l = [0 for _ in range(20)]
print(l)

# we want.... [0, 1, 0, 1, 0, 1]
print([(0, 1) for _ in range(20)])
# so that has these tuples in it....
print([0, 1] * 20)

print(["x"] * 20)

height, width = 20, 10

# matrix = []
# for _ in range(height):
#     matrix.append([0] * width)

# print(matrix)

matrix = []
for _ in range(height):
    matrix.append([0] * width)

matrix[15][3] = 45
print(matrix)

matrix = []
for _ in range(height):
    row = [0] * width
    col_index = random.choice(range(width)) # you would really use index for this
    row[col_index] = random.randint(0,100) # but you would look this up from the data
    matrix.append(row)

for row in matrix:
    print(row)