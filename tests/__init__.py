'''
This is possibly a bad idea hiding this in here
but it's cool
'''
import unittest

from stormtrooper.process import *
from stormtrooper.support import *
from stormtrooper.finding import *
from stormtrooper.results import *

__all__ = ['unittest', 'BaseTest']

class BaseTest(unittest.TestCase):
    '''
    The base test for all my unittests
    hidden in this init file ^_^
    '''
    
    def setUp(self):
        self.logger = Logger(True)
        
        self.r1 = r'a.c'
        self.lines1 = ['this is a file',
                       'line abc 2',
                       'not a match',
                       'garbage'
        ]
        self.processor1 = Processor([self.r1])
        
        r1 = r".abc."
        r2 = r"1234"
        f1 = "main.java"
        f2 = "class.java"
        self.finding1 = Finding(regex=r1, file_name=f1, line=(1, "abcabc"))
        self.finding2 = Finding(regex=r1, file_name=f2, line=(6, "abcdef"))
        self.finding3 = Finding(regex=r2, file_name=f1, line=(2, "12341234"))
        self.finding4 = Finding(regex=r2, file_name=f1, line=(4, "1234 this is a line"))
        self.finding5 = Finding(regex=r2, file_name=f2, line=(51, "EOF 1234"))
        self.findings = Findings('Unit test', [
                                  self.finding1, 
                                  self.finding2, 
                                  self.finding3,
                                  self.finding4,
                                  self.finding5
        ])