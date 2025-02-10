infile = open('stuff.txt', 'r', encoding='utf-8')
text = infile.read()
infile.close()

## I could use the with block for this

with open('stuff.txt', 'r', encoding='utf-8') as infile:
    text = infile.read()


import pathlib

p = pathlib.Path('stuff.txt')

print(p)
print(type(p))

print(p.exists())
print(p.is_dir())

## inspect file paths and names

print(p.name)

print(p.stem, p.suffix)

print(p.parent)
print(p.absolute())
print(p.suffixes)

## pathlib and dirs

d = pathlib.Path('my_new_folder')
print(d.absolute())
print(d.exists())
d.mkdir(exist_ok=True)

for letter in "abcdefg":
    # print(letter + ".txt")
    p = d / (letter + ".txt")
    print(p.absolute())
    p.write_text("here's a letter: " + letter)