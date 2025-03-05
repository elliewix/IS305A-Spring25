
# count = 0
# for _ in range(27):
#     count += 1
#     print(count)
#     if count == 3:
#         count = 0

# count the number of groups
num_groups = 0
count = 0
for _ in range(27):
    count += 1  #increment
    print(count)
    if count == 3:
        num_groups += 1 # collection
        count = 0 # reset
print("total number of groups", num_groups)

## let's read in some data

with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    data = infile.read()

lines = data.splitlines()

print(lines)
#
# groups = []
# temp = []
# # let's add in something to see strays
# lines.append("stray 1")
# for l in lines:
#     temp.append(l) # increment
#     print(temp)
#     if len(temp) == 3:
#         groups.append(temp) # collect
#         temp = [] # reset
# print("final value of temp", temp)
# print("our groups of 3 are", groups)

# let's handle strays

groups = []
temp = []
# let's add in something to see strays
lines.append("stray 1")
lines.append("stray 2")
lines.append("stray 3")
for l in lines:
    temp.append(l) # increment
    print(temp)
    if len(temp) == 3:
        groups.append(temp) # collect
        temp = [] # reset

# groups.append(temp) # caution this will add even when empty
if temp: # thruthiness
    groups.append(temp)
print("final value of temp", temp)
print("our groups of 3 are", groups)

## double checking we got everything
flat = []
for g in groups:
    flat += g
flat2 = []
[flat2.extend(g) for g in groups]

assert len(lines) == len(flat)
print(len(lines), len(flat), len(flat2))

# another thing for comps

with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    data = infile.readlines()

# print(data)

lines = [row.strip() for row in data]
print(lines)

with open('dodec_mangled.dat', 'rt', encoding='utf-8') as infile:
    lines = [row.strip() for row in infile]

print(lines)

##