import httplib2, urllib 
from bs4 import BeautifulSoup 
import os 
import json
import time

access_token='EAALAj7j7JQgBAIWRfYwubfzVq3wfeZCpdzZB9uMx0MmtgwNMg6g5xWH5Apgqkf9ZBPhjkmSJXmhSQ4riONKQK6B900x1euSkrcp8um8ZAf6CX64sEG0Ooj7ZBYzZA3rvuMAYD3eyvwZBczmFSe4EI8FzKla7Q9ABS3Pm3kMRLcKNJ1ePjPaCKFmxS5yzZCB2nabV4WyOE5a84gZDZD'
# access_token = raw_input('Paste your access token here :')

conn = httplib2.HTTPSConnection("graph.facebook.com") 
print('Please Wait!')
 
def comment(url): 
    connect = httplib2.HTTPSConnection("graph.facebook.com") 
    connect.request("GET",url) 
    for x in xrange(1000): # make it 10, 100, 1000, 10000  
            
            print('commenting %d ')% x
            path ='/'+'1225266307840650'+'/comments'
            param_data={  'format':'json', 
                        'message':'5k Hobe', # change message from here
                        'access_token':access_token 
                  } 
            connect = httplib2.HTTPSConnection("graph.facebook.com") 
            connect.request("POST",path,urllib.urlencode(param_data),{}) 
            time.sleep(0.09)
           
url='1225266307840650' 
comment(url) 
print('DONE!')
