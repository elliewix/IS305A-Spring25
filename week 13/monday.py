from lxml import etree

with open('hamlet-tei.xml', 'rb') as infile:
    xml = infile.read()
    tree = etree.fromstring(xml)

print(tree)

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

# your general pattern
# tree.xpath('your xpath query', namespaces = ns)
query = tree.xpath('//text()', namespaces = ns )
# print(query)

all_sp = tree.xpath('//tei:sp', namespaces = ns)
print(len(all_sp))
all_ham = tree.xpath('//tei:sp[@who = "#F-ham-ham"]', namespaces = ns)
print(len(all_ham))
