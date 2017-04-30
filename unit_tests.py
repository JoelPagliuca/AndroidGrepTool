'''
Created on 16/09/2015

@author: JoelPagliuca
'''
import unittest

tests = unittest.defaultTestLoader.discover("tests", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)