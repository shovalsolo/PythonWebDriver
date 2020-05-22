# Example of multiple conditions elif is else if



province = input('Province name?')
province.capitalize()


if province == 'Alberta':
    tax = 0.07    
    print( 'tax is: ' + str(tax))

elif province == 'Nunavut':
    tax = 0.05
    print('tax is: ' + str(tax))
    

elif province == 'Ontario':
    tax = 0.13
    print('tax is: ' + str(tax))
    
else:
    tax = 0.15
    print('tax is: ' + str(tax))
    