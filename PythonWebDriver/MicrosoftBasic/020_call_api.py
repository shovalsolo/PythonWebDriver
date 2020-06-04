# This is an example of an api call with python

import requests
import json
import pprint 

base_url = 'https://reqres.in'
 
users_reqsuest = '/api/users?page=2'
 
url_reqsuest = base_url + users_reqsuest

r = requests.get(url_reqsuest)
print()
print('--------------All the call--------------')
print(r.json())                                                         #getting all the response from json
print()
print('--------------All the call-------------------')
pprint.pprint(r.json())                                                 #getting all the response from json formatted
print()
print('---------The call only the data part------')                     
pprint.pprint(r.json()['data'])                                         #The call only the data part
print()
print('---The call only the location zero in the data---')              
pprint.pprint(r.json()['data'][0])                                      #The call only the location zero in the data
print()
print('---The call only the location zero in the data avatar image---') 
pprint.pprint(r.json()['data'][0]['avatar'])                            #The call only the location zero in the data avatar image
