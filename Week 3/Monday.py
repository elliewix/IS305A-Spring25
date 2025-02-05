print("hello world")

###
# python list review

# make an empty list
l = [] # list()
# # don't use a function name as a var
# list = []
# print(list("abc"))

my_list = []
# grow or shrink in size as you use them
my_list.append("stuff")
print(my_list)

# no data types to declare

letters = list("abcdefg")
print(letters)

for l in letters:
    print(l)

# don't want to see the following
# when it doesn't make sense
for i in range(len(letters)):
    print(letters[i])

## if you really need that index position

for i, l in enumerate(letters):
    print(i, l)

## indexing
print(letters[0])
print(letters[4])
## slicing
print(letters[1:4])

##
letters_1 = list("abcd")
letters_2 = list("wxyz")

print(letters_1)
print(letters_2)

### ummm how do we combine these?

print(letters_1 + letters_2) # not the pairs that I want

# this will loop but not the content together
for l in letters_1:
    print(l)
for l in letters_2:
    print(l)

# pro: pairs, con: of all of them
for l in letters_1:
    for other_l in letters_2:
        print(l, other_l)

## mutual index pattern, as named in homework

print(letters_1)
print(letters_2)
for i in range(len(letters_1)):
    print(i)
    print(letters_1[i], letters_2[i])

