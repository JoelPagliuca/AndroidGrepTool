'''
Created on 18/09/2015

@author: JoelPagliuca
'''
from tests import *

class TestCriterion(BaseTest):

    def test_search_lines(self):
        matches = self.processor1.search_lines(self.r1, self.lines1)
        self.assertEqual(len(matches), 2)
        self.assertIsInstance(matches[0], tuple)
        self.assertIn((2, 'line abc 2'), matches)
        
        matches = self.processor1.search_lines(self.r1, [""])
        self.assertEqual(len(matches), 0)

if __name__ == "__main__":
    unittest.main()