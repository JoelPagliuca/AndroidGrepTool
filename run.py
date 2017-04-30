'''
Created on 16/09/2015

Project that checks an Android app directory for
things a pentester should inspect

@author: JoelPagliuca
'''
import os
from stormtrooper.driver import Driver

if __name__ == '__main__':
    output_file = "output.xml"
    app_directory = 'test_app_directory'
    transform = 'html_transform.xslt'
    
    app = Driver(app_directory, output_file)
    app.start()
    
    # convert the output xml to html with Saxon
    saxon = "java -jar saxon9he.jar -xsl:{0} -s:{1} -o:{2}".format(transform, output_file, "output.html")
    os.system(saxon)