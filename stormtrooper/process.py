'''
Created on 16/09/2015

@author: JoelPagliuca
'''
import re

from stormtrooper.finding import Finding

__all__ = ["Processor"]

class Processor(object):
    '''
    Something we will search for and then include in results
    '''

    def __init__(self, regexes):
        '''
        Constructor
        
        @param regexes: list
        '''
        self.regexes = regexes
    
    def search_lines(self, regex, lines):
        '''
        @param lines: list
        @return: list
        '''
        results = []
        n = 1 # line number
        for line in lines:
            if re.search(regex, line):
                results.append((n, line))
            n += 1
        return results
        
    def search(self, file_names):
        '''
        opens and greps the files
        
        @param file_names: list
        @rtype: list
        @return: findings of the search
        '''
        findings = []
        for file_name in file_names:
            fp = open(file_name, 'r')
            file_lines = fp.readlines()
            for regex in self.regexes:
                matched_lines = self.search_lines(regex, file_lines)
                for m in matched_lines:
                    findings.append(Finding(regex=regex, file_name=file_name, line=m))
            fp.close()
        return findings