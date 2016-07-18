#-*- coding: utf-8 -*-

import unittest
import yaml
from epgen.confgen import generate_config

class TestConfGen(unittest.TestCase):
    def test_generate_config(self):
        project_name = 'lightmw-sdk'
        project_rootdir = '/User/jhkang/works/lightmw-sdk/g4'
        build_target = 'linux_headless'

        generate_config(project_name, project_rootdir, build_target)

        with open('config') as f:
            conf = yaml.load(f)
            self.assertEquals(conf['name'], project_name)
            self.assertEquals(conf['rootdir'], project_rootdir)

            for d in conf['classpaths']:
                builddir = 'build/%(build_target)s' % locals()
                if d['kind'] == 'lib':
                    self.assertTrue(d['path'].startswith(builddir))
            
if __name__ == '__main__':
    unittest.main()
