'''
Created on 16/09/2015

Module with useful support functionality

@author: JoelPagliuca
'''
# I dunno wtf is happening with this import
# from datetime.datetime import now

__all__ = ["Logger"]

class Logger(object):
    '''
    The logger I keep implementing
    '''
    def __init__(self, d_flag):
        self.d_flag = d_flag
    
    def debug(self, msg, tag="DEBUG"):
        if self.d_flag:
            print "[{}] [{}] {}".format(get_time(), tag, msg)
            return True

def get_time():
#     h = now().hour
#     m = now().minute
#     s = now().second
    return "{}:{}:{}".format('h', 'm' , 's')