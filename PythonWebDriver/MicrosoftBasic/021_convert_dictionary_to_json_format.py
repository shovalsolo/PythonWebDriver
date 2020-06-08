# This is an example of how to convert a dictionary to a json format

import requests
import json
import pprint 


person_dictionary = {'first':'Chris' , 'last':'Zo'}                     #creating a dictionary

person_dictionary['city'] = 'Orlando'                                   # adding a new key and value to the dictionary

person_json = json.dumps(person_dictionary)                             #converting dictionary to json

print()
print('----printing the json object----')
print(person_json)                                                      #printing the json object
