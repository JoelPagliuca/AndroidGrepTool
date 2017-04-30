'''
Created on 18/09/2015

Configuration for the checks to perform

@author: JoelPagliuca
'''
CATEGORIES = [
    {
     'name':'Weird permissions',
     'type':'manifest',
     'checks': [
        {'regex':'CALL_PHONE'},
        {'regex':'SEND_SMS'},
        {'regex':'RECEIVE_BOOTLOADED'}]
     },
    {
     'name':'Exported Activities',
     'type':'manifest',
     'checks': [
        {'regex':'exported=\"true\"'}]
     },
    {
     'name':'Bad practises',
     'type':'java',
     'checks': [
        {'regex':'WebView'}]
     },
    {
     'name':'Unauthorized access',
     'type':'java',
     'checks': [
        {'regex':'os\..*system'}]
     },
    {
     'name':'Proper SSL',
     'type':'java',
     'checks': [
        {'regex':'X509TrustManager'},
        {'regex':'X509Certificate'}]
     }
]