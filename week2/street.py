# -*- coding: utf-8 -*-
import codecs
f = codecs.open('stree.txt', 'r', 'cp1251')
street_names = []
for line in f:
    street_names.append(line.encode('utf-8'))

for name in street_names:
    print name.decode('utf-8')
print street_names