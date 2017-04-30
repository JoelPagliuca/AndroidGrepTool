'''
Created on 19/09/2015

@author: JoelPagliuca
'''
import os, re

from stormtrooper import LOGGER
from stormtrooper.process import Processor
from stormtrooper.finding import Findings
from stormtrooper.results import findings_to_xml, write_xml

JAVA = ".*\.java"
MANIFEST = "AndroidManifest\.xml"

class Driver(object):
    '''
    Makes everything happen between config and results
    '''

    def __init__(self, directory, output_file):
        '''
        Constructor
        
        @param directory: str
        '''
        self.output_file = output_file
        self.file_paths = {
           'java' : [],
           'manifest' : []
        }
        for dirname, _, filenames in os.walk(directory):
            for filename in filenames:
                file_path = os.path.join(dirname, filename)
                if re.search(JAVA, filename):
                    self.file_paths['java'].append(file_path)
                if re.search(MANIFEST, filename):
                    self.file_paths['manifest'].append(file_path)
    
    def start(self):
        '''
        '''
        import config
        tag = "DRIVER"
        
        all_findings = []
        for category in config.CATEGORIES:
            LOGGER.debug("category: "+category['name'], tag)
            processors = []
            file_list = self.file_paths[category['type']]
            # generate the Processor object
            regexes = []
            for check in category['checks']:
                regexes.append(check['regex'])
            p = Processor(regexes)
            processors.append(p)
            LOGGER.debug("-made {} processors".format(len(processors)), tag)
            # run the processors on the files
            for p in processors:
                search_results = p.search(file_list) # Finding[]
                if search_results:
                    findings = Findings(category['name'], search_results)
                    all_findings.append(findings)
            LOGGER.debug("-currently at {} Findingss".format(len(all_findings)), tag)
        
        xml_data = []
        for a in all_findings:
            xml_data.append(findings_to_xml(a))
        
        write_xml(xml_data, self.output_file)