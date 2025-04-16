from lxml import etree

with open('hamlet-tei.xml', 'rb') as infile:
    xml = infile.read()
    tree = etree.fromstring(xml)

# print(tree)
ns = {'tei': 'http://www.tei-c.org/ns/1.0'}

stage_dir_text = tree.xpath('//tei:stage/text()', namespaces = ns)
print(stage_dir_text)
print(len(tree.xpath('//tei:stage', namespaces = ns)))
print(len(tree.xpath('//tei:stage/text()', namespaces = ns)))
print(len(tree.xpath('//tei:stage//text()', namespaces = ns)))
print(len(tree.xpath('//tei:stage/@type', namespaces = ns)))

stage_nodes = tree.xpath('//tei:stage', namespaces = ns)

all_directions = []
for node in stage_nodes:
    # print(node.xpath('@type'), node.xpath('.//text()', namespaces = ns))
    stage_type = node.xpath('@type')
    text = node.xpath('.//text()', namespaces = ns)
    # print(stage_type, "".join(text))
    all_directions.append([stage_type, "".join(text)])
# so I didn't deal with the missing type direction
print(len(all_directions))

