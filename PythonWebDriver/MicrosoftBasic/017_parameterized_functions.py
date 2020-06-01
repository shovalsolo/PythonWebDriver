# Example of Parameterized functions


def get_initial(name, force_uppercase=True):                                #A function that is getting 2 params one string and one true false with default of true
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input('Enter your first name: ')
first_name_initial = get_initial(name=first_name, force_uppercase=False)    #Sending the string and true or false if we want upper case

print('Your initials are: ' + first_name_initial)



