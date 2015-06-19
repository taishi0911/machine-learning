# -*- coding: utf-8 -*-

import urllib2, sys
import xml.etree.ElementTree as etree
# import codecs

try: zipcode = sys.argv[1]
except: zipcode = '1700003'
reap = urllib2.urlopen('http://zip.cgis.biz/xml/zip.php?zn=%s'%zipcode).read()

output = {}
tree = etree.fromstring(reap)

for e in tree[-1]:
	output[e.attrib.keys()[0]] = e.attrib.values()[0]

# sys.stdout = codecs.getwriter("utf-8")("sys.stdout")
print output
print output["state"]+output["city"]+output["address"]