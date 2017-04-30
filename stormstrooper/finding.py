'''
Created on 16/09/2015

@author: JoelPagliuca
'''

__all__ = ['Finding', 'Findings']

class Finding(object):
    '''
    An object representing the finding of a search
    '''

    def __init__(self, **kwargs):
        '''
        Constructor
        TODO: Existance checking
        '''
        self.regex = kwargs['regex']
        self.file_name = kwargs['file_name']
        self.line = kwargs['line']

class Findings(object):
    '''
    A group of findings
    '''
    
    def __init__(self, title, findings):
        '''
        @param title: str
        @param findings: list
        '''
        self.title = title
        self._findings = findings
    
    def get_regexes(self):
        '''
        @rtype: list
        '''
        results = []
        for f in self._findings:
            if f.regex not in results:
                results.append(f.regex)
        return results
    
    def get_files(self, regex):
        '''
        @param regex: str
        @rtype: list
        @return: the file_names that included the regex
        TODO: Code smell
        '''
        results = []
        for f in self._findings:
            if f.regex == regex and f.file_name not in results:
                results.append(f.file_name)
        return results
    
    def get_lines(self, file_name, regex):
        '''
        @param file_name: str
        @param regex: str
        @rtype: list
        @return: the (number, line) within the file that included the regex
        '''
        results = []
        for f in self._findings:
            if f.regex == regex:
                if f.file_name == file_name:
                    results.append(f.line)
        return results