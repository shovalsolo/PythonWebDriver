# Example of dictionaries of type collection the difference is that we have key and value pairs of items and the stored order is not guaranteed 

#        Key        Value
person = {'first' : 'Chris'}

person['last'] = 'Harison'                      #appending a new key and value

print(person)

print(person['first'])

car = {}
car ['Make'] = 'Mazda'
car ['Model'] = 'x6'

print(car)

all = []                                        #Creating an empty list
all.append(person)                              #inserting the dictionary person in to a list names all
all.append(car)                                 #inserting the dictionary car in to a list names all
all.append({'first' : 'Bill', 'last' : 'Gates'})#appending a new dictionary in to the list

print(all)