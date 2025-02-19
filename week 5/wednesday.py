data = {}

for letter in "abcdefg":
    fname = letter + ".txt"
    content = "hello I am the letter " + letter
    data[fname] = content

# for filename, content in data.items












new_string = ""
source = "here's some r0ugH 1ex1"
for character in source:
    print(character, character.isalpha())
    if character.isalpha():
        new_string += character

print(new_string)
#####
source = "here's some r0ugH 1ex1"
# oops repeated values, let's get the uniques
letter_list = list(source)
print(letter_list)
unique_letters = set(letter_list)
print(unique_letters)

data = {}
for character in unique_letters:
    # print(character)
    data[character + ".txt"] = character + ":" + str(letter_list.count(character))

print(data)
import pathlib

for filename, content in data.items():
    print(filename, content)
    p = pathlib.Path(filename)
    p.write_text(content)