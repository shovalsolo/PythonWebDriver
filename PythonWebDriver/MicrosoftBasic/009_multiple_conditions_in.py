# Example of multiple conditions in



province = input('Province name? ')
province.lower()
tax = 0


if province in ('alberta','nunavut','yukon'):
    tax = 0.05   
    print( 'tax is: ' + str(tax))

    
elif province == 'ontario':
    tax = 0.13
    print('tax is: ' + str(tax))
    
else:
    tax = 0.15
    print('tax is: ' + str(tax))
    