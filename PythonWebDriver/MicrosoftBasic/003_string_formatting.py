# Example for formatting 

first_name = input('What is your first name: ')
last_name = input('What is your last name: ')

#Using the regular way without formatting
output = 'hello, ' + first_name + ' ' + last_name
print(output) 

#using a place holder for the params
output = 'hello, {} {}' .format(first_name, last_name)
print(output)

#using a place holder for the params
output = 'hello, {0} {1}' .format(first_name, last_name)
print(output)

#Only in python 3 the f is for the formatting
output = f'hello,  {first_name} {last_name}' 
print(output)