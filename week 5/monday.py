import csv

with open('pokemon_names_and_descriptions.csv', 'rt', encoding='utf-8') as infile:
    headers, *data = csv.reader(infile)

print(headers)
print(len(data))

all_pokedex_nums = []
for row in data:
    dex = row[0]
    all_pokedex_nums.append(dex)
    # print(dex)
print(all_pokedex_nums)

for dex in all_pokedex_nums:
    if dex.isnumeric():
        print(dex)

only_alnum_names = []
bad_alnum_rows = []
for row in data:
    name = row[1]
    if name.isalnum():
        only_alnum_names.append(name)
        # print(name)
    else:
        bad_alnum_rows.append(row)

print("how many alnum names", len(only_alnum_names))

## writing out a csv file

# 2 things to have first: headers and a 2d list of data

with open('alnum_failures.csv', 'wt', encoding='utf-8', newline="") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(bad_alnum_rows)
