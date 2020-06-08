# This is an example of how to convert a dictionary to a json format

import requests
import json
import pprint 


person_dictionary = {'first':'Chris' , 'last':'Zo'}                     #creating a dictionary

person_dictionary ['city'] = 'Orlando'                                  #adding a new key and value to the dictionary

staff_dictionary = {}                                                   #creating an empty dictionary

staff_dictionary ['Program manager'] = person_dictionary                #assigning the person_dictionary to the staff_dictionary

person_json = json.dumps(person_dictionary)                             #converting dictionary to json

stuff_json = json.dumps(staff_dictionary)                               #converting dictionary to json

print()
print('----printing the json object----')
print(person_json)                                                      #printing the json object person_dictionary


print()
print('----printing the json object with the staff_dictionary----')
print(stuff_json)                                                       #printing the json object staff_dictionary


languahes_list = ['CSharp' , 'Python' , 'Java']                         #creating a list

person_dictionary ['languages'] = languahes_list                        #Adding the list to the dictionary

person_json = json.dumps(person_dictionary)                             #converting dictionary to json
print()
print('----printing the json object with the language list----')
print(person_json)                                                      #printing the json object person_dictionary
