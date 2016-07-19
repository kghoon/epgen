# -*- coding: utf-8 -*-

'''
  project file generator
  ~~~~~~~~~~~~~~~~~~~~~~

  :copyright: (c) 2016 by Jihoon Kang <kang@ghoon.net>
  :license: Apache 2, see LICENSE for more details
'''

from xml.etree import ElementTree
from xml.dom import minidom
from jinja2 import Environment, FileSystemLoader
import re

def generate_project(configs, output):
    env = Environment(loader=FileSystemLoader('./templates'),
            trim_blocks=True)
    tmpl = env.get_template('project')
    root = ElementTree.fromstring(tmpl.render(configs))
    linkedResources = root.find("linkedResources")

    for entry in configs['links']:
        node = ElementTree.SubElement(linkedResources, 'link')

        name = ElementTree.SubElement(node, 'name')
        name.text = entry['name']

        typeNode = ElementTree.SubElement(node, 'type')
        typeNode.text = '2'

        location = ElementTree.SubElement(node, 'location')
        location.text = "%s/%s" % (configs['rootdir'], entry['location'])

    with open(output, 'w') as f:
        xmlstr = ElementTree.tostring(root)
        # remove all whitespaces before beautifying
        xmlstr = re.sub(r'>\s+', '>', xmlstr)
        xmlstr = minidom.parseString(xmlstr).toprettyxml(indent="\t")
        print xmlstr
        f.write(xmlstr.encode('utf-8'))
