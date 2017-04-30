'''
Created on 16/09/2015

@author: JoelPagliuca
'''
from xml.etree import ElementTree as ET

from androidgrep import LOGGER

def findings_to_xml(findings):
    '''
    Converts the Findings into a viewable format
    see Notes for XML structure
    this makes me just as sick as you
    
    @param findings: Findings
    @rtype: ElementTree.Element
    '''

    tag = "TO_XML" # debug tags
    cat = ET.Element("category", {"title":findings.title})
    LOGGER.debug("making xml for {}".format(findings.title), tag)
    checks = ET.Element("checks")
    for reg in findings.get_regexes():
        LOGGER.debug("making element for "+reg, tag)
        check = ET.Element("check", {"regex":reg})
        for fname in findings.get_files(reg):
            LOGGER.debug("results for: "+fname, tag)
            fel = ET.Element("file", {"name":fname})
            for (number, line) in findings.get_lines(fname, reg):
                lel = ET.Element("line", {"number":str(number)})
                lel.text = line
                fel.append(lel)
            check.append(fel)
        checks.append(check)
    cat.append(checks)
    
    return cat

def write_xml(elements, fname):
    '''
    @param elements: list (ElementTree.Element)
    @param fname: str
    '''
    root = ET.Element("androidgrep")
    for e in elements:
        root.append(e)
    et = ET.ElementTree(root)
    et.write(fname)