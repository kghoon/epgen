# -*- coding: utf-8 -*-

'''
  Config file generator
  ~~~~~~~~~~~~~~~~~~~~~

  :copyright: (c) 2016 by Jihoon Kang <kang@ghoon.net>
  :license: Apache 2, see LICENSE for more details
'''

from jinja2 import Environment, FileSystemLoader
import yaml

def generate_config(project_name, project_rootdir, build_target,
        tmpl_name='default', tmpl_dir='configs', output='config'):

    env = Environment(loader=FileSystemLoader(tmpl_dir),
            trim_blocks=True)
    tmpl = env.get_template('%(tmpl_name)s.config' % locals())

    with open(output, 'w') as f:
        f.write(tmpl.render(locals()))

def read_config(filename):
    with open(filename) as f:
        configs = yaml.load(f)
        return configs

