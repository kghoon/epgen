# -*- coding: utf-8 -*-

'''
  Config file generator
  ~~~~~~~~~~~~~~~~~~~~~

  :copyright: (c) 2016 by Jihoon Kang <kang@ghoon.net>
  :license: Apache 2, see LICENSE for more details
'''

from jinja2 import Environment, FileSystemLoader

def generate_config(project_name, project_rootdir, build_target,
        tmpl_name='default'):

    env = Environment(loader=FileSystemLoader('./configs'),
            trim_blocks=True)
    tmpl = env.get_template('%(tmpl_name)s.config' % locals())

    with open('config', 'w') as f:
        f.write(tmpl.render(locals()))

