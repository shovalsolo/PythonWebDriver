# Example of functions

from datetime import datetime

def print_time():                           #A function that is printing the time 
    print('Task completed')
    print(datetime.now())
    print()
    
def print_message(task_name):               #A function that is getting a string and printing it and the time
    print(task_name)
    print(datetime.now())
    print()
    
def get_initial(name):                      #A function that is getting a name and returning the first letter
    initial = name[0:1].upper()
    return initial



first_name = 'Su'
print_message('first name assigned')        #Calling the print_message function with a string
print_time()                                #Calling the function


for x in range(0, 10):                      #A for loop that is running in a range 
    print(x)
    
print_message('loop completed')             #Calling the print_message function with a string
print_time()                                #Calling the function


first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')

print('Your full name is: ' + first_name + ' ' + last_name)
print('Your initials are: ' + get_initial(first_name) + get_initial(last_name))



