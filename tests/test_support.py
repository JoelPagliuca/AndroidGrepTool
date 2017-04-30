'''
Created on 16/09/2015

@author: JoelPagliuca
'''
from tests import *

class TestLogger(BaseTest):

    def testDebug(self):
        self.assertIsNotNone(self.logger.debug("SOMETHING"), "Logger didn't print")

if __name__ == "__main__":
    unittest.main()