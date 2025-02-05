left =  list("abcdefghijkl")
right = list("aoeuidhhtns-")
other = list("stuff")

print(len(left), len(right))
assert len(left) == len(right)
# assert len(left) == len(other), "lengths don't match" # produces an error


print(type(left) == list)

##

print(left)
print(right)

# mutual index
for i in range(len(left)):
    print(left[i], right[i])
    l = left[i]
    r = right[i]

for i, l in enumerate(left):
    r = right[i]
    print(l, r)

# zip style

# zip is a function and it takes sequences

print(list(zip(left, right)))

for l, r in zip(left, right):
    print(l, r)

print(list(zip(left, other)))

### function definitions

# define a function that take a bill amount and splits it in half

def split_bill_in_half(bill):
    half = bill /2
    return half

print(split_bill_in_half(35))

# if statements and style

