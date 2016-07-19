# -*- coding: utf-8 -*-

'''
  classpath file generator
  ~~~~~~~~~~~~~~~~~~~~~~~~

  :copyright: (c) 2016 by Jihoon Kang <kang@ghoon.net>
  :license: Apache 2, see LICENSE for more details
'''
from xml.etree.ElementTree import parse, Element, dump
from xml.etree import ElementTree
from xml.dom import minidom
import re
def generate_classpath(configs, output):
    tree = parse('./templates/classpath')
    root = tree.getroot()

    for entry in configs['classpaths']:
        node = Element('classpathentry')
        for key in entry.keys():
            node.attrib[key] = entry[key]
        root.append(node)

    with open(output, 'w') as f:
        xmlstr = ElementTree.tostring(root)
        # remove all whitespaces before beautifying
        xmlstr = re.sub(r'>\s+', '>', xmlstr)
        xmlstr = minidom.parseString(xmlstr).toprettyxml(indent="\t")
        f.write(xmlstr.encode('utf-8'))

