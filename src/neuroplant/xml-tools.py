from lxml import etree

tree = etree.parse("../../data/meta/band2_meta.xml")
root = tree.getroot()
print len(root)
for i in root:#.findall('mets:Flocat', root.nsmap):
    print i.tag
