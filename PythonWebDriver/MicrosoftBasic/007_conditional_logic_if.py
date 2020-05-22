# Example for conditional logic if
# Greater than             >
# Less than                <
# Greater than or equal to >=
# less than or equal to    <=
# is equal to              ==
# is not equal to          !=


price = input('How much did you pay?')
price = float(price)

#if
if price >= 1.00:
    tax = .07
    
    print( 'tax is: ' + str(tax))
    print('price is: ' + str(price))

else:
    tax = 0
    
    print('tax is: ' + str(tax))
    print('price is: ' + str(price))
    
print()
country = 'CANADA'
if country.lower() == 'canada':
    print('Oh look a Canadian')
else:
    print('You are not from Canada')