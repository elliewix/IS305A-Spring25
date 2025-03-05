count = 0
for i in range(27):
    count += 1
    print(count)
    if count == 3:
        print("found a group", count, i)
        count = 0


# collect some actual data

groups = []
temp_group = []
for i in range(27):
    temp_group.append(i)
    if len(temp_group) == 3:
        print("group", temp_group)
        groups.append(temp_group)
        temp_group = []

print(groups)

# what about when you have an uneven number of groups?
# honestly there's a few ways to handle this
groups = []
temp_group = []
for i in range(27):
    temp_group.append(i)
    if len(temp_group) == 3:
        print("group", temp_group)
        groups.append(temp_group)
        temp_group = []

if temp_group:
    groups.append(temp_group) # you can just add it on here

print(groups)

## let's read in a file for this

with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    data = [l.strip() for l in infile]

groups = []
temp_group = []
for line in data:
    temp_group.append(line)
    if len(temp_group) == 3:
        print(temp_group)
        groups.append(temp_group)
        temp_group = []

print(groups)
print(temp_group)

# what if we added some random data to the end?

data.append('extra 1')
data.append('extra 2')

# so this is no longer divisible by 3

groups = []
temp_group = []
for line in data:
    temp_group.append(line)
    if len(temp_group) == 3:
        print(temp_group)
        groups.append(temp_group)
        temp_group = []
if temp_group:
    groups.append(temp_group)

print(groups)

# however, we can also check to see if we've run out of data


groups = []
temp_group = []
for i, line in enumerate(data): # we need the index for this
    temp_group.append(line)
    if len(temp_group) == 3:
        print(temp_group)
        groups.append(temp_group)
        temp_group = []
    elif (i + 1) == len(data):
        groups.append(temp_group)

print(groups)

## we can also change this to give us access to the upcoming data
## generate some random data for this
import random
random.seed(64)
data = random.choices(range(10),k = 25)
# # let's force it to end with 0
# data.append(0)
print(data)
## all groups should start with a 0, so if the next one is a 0, collect and reset
groups = []
temp_group = []
for i, num in enumerate(data):
    temp_group.append(num)
    if (i + 1) != len(data): # midlands
        upcoming = data[i + 1]
        if upcoming == 0:
            groups.append(temp_group)
            temp_group = []
    else: # at the end
        groups.append(temp_group)

print(groups)