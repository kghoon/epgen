#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
  epgen runtime
  ~~~~~~~~~~~~~

  :copyright: (c) 2016 by Jihoon Kang <kang@ghoon.net>
  :license: Apache 2, see LICENSE for more details
'''

import os
import argparse

from cpgen import *
from confgen import *
from prgen import *

class EpgenRuntime:
    TMPL_DIR = './templates'

    target_dir = './output'
    config_output = './config'
    config_tmpl = 'default'
    install_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
    current_path = os.getcwd()
    config_file = None
    confgen_mode = False

    def start(self):
        self.parse_args()
        if self.confgen_mode:
            self.generate_config()
        else:
            self.read_config()
            self.make_dirs()
            self.generate_classpath()
            self.generate_project()
            self.copy_rest_templates()

    def parse_args(self):
        parser = argparse.ArgumentParser(description='generate eclipse project templates')
        group = parser.add_mutually_exclusive_group(required=True)
        group.add_argument('--config', nargs='?', help="generate config file with given CONFIG template")
        group.add_argument('config_file', nargs='?', help="generate project templates using the config file")
        parser.add_argument('--workroot', nargs='?', help="project root directory", default="<work-root>")
        parser.add_argument('--name', nargs='?', help="project name", default="<project-name>")
        parser.add_argument('--buildtarget', nargs='?', help="build target. alticast build system specific information", default="<build-target>")
        args = parser.parse_args()

        if not args.config_file:
            self.confgen_mode = True
            if args.config:
                self.config_tmpl = args.config
        else:
            self.config_file = args.config_file

        self.project_name = args.name
        self.project_rootdir = args.workroot
        self.build_target = args.buildtarget

    def generate_config(self):
        tmpl_dir = '%s/configs' % self.install_path

        generate_config(self.project_name, self.project_rootdir,
                self.build_target, self.config_tmpl, tmpl_dir)

    def read_config(self):
        self.configs = read_config(self.config_file)
        self.target_dir = self.configs['name']

    def make_dirs(self):
        os.system("mkdir -p %s/settings" % self.target_dir)

    def generate_classpath(self):
        generate_classpath(self.configs, "%s/.classpath" % self.target_dir)

    def generate_project(self):
        tmpl_dir = '%s/templates' % self.install_path
        generate_project(self.configs, "%s/.project" % self.target_dir, tmpl_dir)

    def copy_rest_templates(self):
        settings_dir = "%s/settings" % self.TMPL_DIR

        for root, dir, files in os.walk(settings_dir):
            for f in files:
                src_file = os.path.join(root, f)
                dst_dir = os.path.join('%s/settings/' % self.target_dir)
                os.system("cp -f %(src_file)s %(dst_dir)s" % locals())


if __name__ == '__main__':
    EpgenRuntime().start()
