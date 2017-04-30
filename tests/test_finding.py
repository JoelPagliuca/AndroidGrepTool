'''
Created on 17/09/2015

@author: JoelPagliuca
'''
from tests import *

class TestFinding(BaseTest):

    def test_get_regexes(self):
        l = self.findings.get_regexes()
        self.assertEqual(len(l), 2)
        self.assertIsInstance(l[0], str)
    
    def test_get_files(self):
        l = self.findings.get_files(r".abc.")
        self.assertEqual(len(l), 2)
        self.assertIsInstance(l[0], str)
    
    def test_get_lines(self):
        l = self.findings.get_lines("main.java", r"1234")
        self.assertEqual(len(l), 2)
        self.assertIsInstance(l[0], tuple)

if __name__ == "__main__":
    unittest.main()