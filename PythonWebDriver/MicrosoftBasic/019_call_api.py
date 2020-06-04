# This is an example of an api call with python

import requests
import json
import pprint                                               #an import to format the json


r = requests.get('https://api.dailysmarty.com/posts')       #setting the url for the call
print('--------------All the posts--------------')
print(r.json())                                             #getting all the response from json
print()
print('--------------All the posts-------------------')
pprint.pprint(r.json())                                     #getting all the response but formatting it with pprint
print()
print('--------------Post in location 0--------------')
pprint.pprint(r.json()['posts'][0])                         #getting the response but only the post in location zero
print()
print('--------------URL of Post in location 0----------')
pprint.pprint(r.json()['posts'][0]['url_for_post'])         #getting the response but only the post in location zero the title of the post    




