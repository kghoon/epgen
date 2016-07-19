#-*- coding: utf-8 -*-

import unittest

from epgen.prgen import *
from epgen.confgen import *

class PrGen(unittest.TestCase):
    def test_generate_project(self):
        generate_config('lightmw-sdk', '/home/jhkang/lightmw-sdk', 'linux_headless', 'channel-media')
        configs = read_config('./config')
        generate_project(configs, "test_project.xml")
        pass
