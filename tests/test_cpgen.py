#-*- coding: utf-8 -*-

import unittest
from epgen.cpgen import generate_classpath
from epgen.confgen import *

class TestCpGen(unittest.TestCase):

    def test_generate_classpath(self):
        generate_config('lightmw-sdk', '/home/jhkang/lightmw-sdk', 'linux_headless')
        configs = read_config('./config')
        generate_classpath(configs, "test_classpath.xml")

