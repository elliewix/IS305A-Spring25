import sqlite3

# create a conn object
conn = sqlite3.connect('pettigrew.db')

# create our cursor object

c =  conn.cursor()

# now we can use cursor to get data out

results = c.execute('SELECT * FROM letters;')

print(results)# what's up with this object?
print(range(10))

# these are generator like objects, you need to
# ask or iterate over them to get the stuff

# so if you want to see the data, you need use a
# a fetch command

# print(results.fetchone())
# print(results.fetchmany(5))
# so I would need to comment these two out to get everything
print(results.fetchall())

# how can we tell what tables there are in here?

tables = c.execute('SELECT name FROM sqlite_master where type = "table"')

print(tables.fetchall())

sorted_results = c.execute('SELECT * FROM letters ORDER BY Date;')
# print(sorted_results.fetchall())
# print(sorted_results.fetchall())
# remember that the cursor will stay at the end
# so we can only run through it once
for r in sorted_results.fetchall():
    print(r)

###
# outputting data from results

sorted_results = c.execute('SELECT * FROM letters ORDER BY Date;')
sorted_data = sorted_results.fetchall()
print(len(sorted_data))
import csv
headers = ['box', 'folder', 'contents', 'date']
with open('letters.csv', 'wt', encoding='utf-8', newline="") as outfile:
    csvout = csv.writer(outfile)
    csvout.writerow(headers)
    csvout.writerows(sorted_data)

# let's start with a csv and load that data into a new db

conn = sqlite3.connect('new_letters.db')
c = conn.cursor()

c.execute('CREATE TABLE IF NOT EXISTS letters (folder text, box text, contents text, date text);')

row = ['99', '9', "a letter here", "2025"]
c.execute('INSERT INTO letters VALUES (?, ?, ?, ?)', row)

c.executemany('INSERT INTO letters VALUES (?, ?, ?, ?);', sorted_data)

conn.commit()
conn.close()