#This is an example for strings

sentence = 'enter you name here:'
print(sentence)
print(sentence.upper() + ' to upper case')
print(sentence.lower() + ' to lower case')
print('\n')
print(sentence.capitalize() + ' will capitalize the first letter in the first word')
print(sentence.count('a'))

first_name = input('What is your first name: ')
last_name = input('What is your last name: ')
print('Hello ' + first_name.capitalize() +  ' ' + last_name.capitalize())