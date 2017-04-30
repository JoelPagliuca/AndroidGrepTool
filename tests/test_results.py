'''
Created on 21 Sep 2015

@author: JoelPagliuca
'''
from tests import *
from xml.etree.ElementTree import Element
from androidgrep.results import findings_to_xml

class TestResults(BaseTest):
    
    def test_findings_to_xml(self):
        el = findings_to_xml(self.findings)
        self.assertIsInstance(el, Element)
        self.assertEqual(len(el[0]), 2, "number of children in the view should match number of regexes")
        # I printed it and looked at it, looked pretty legit 2015-09-22

if __name__ == "__main__":
    unittest.main()