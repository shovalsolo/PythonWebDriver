# Example for error handling

#Syntax Error

# x = 42
# y = 298
# if x == y            
# print('Success!!!')         #This will give an error for missing : and will give the problematic area


# #Runtime Error
# 
# x = 42
# y = 0
# print(x / y)                    #This will give a runtime error division by zero and will give the problematic line


#Try/Except/Finally
x = 42
y = 0
try:
    print(x / y)
except ZeroDivisionError as e:                      #This error will show when we divide by zero - ZeroDivisionError is the exception we will get for this flow
        print('Sorry, something went wrong')
else:
    print('Something really went wrong')            #This error will show when we do not divide by zero
finally:
    print('This always runs on success or failure') #This error will show always
    
    
#logic error
x = 206
y = 42
if x < y:
    print(str(x) + 'is greater than ' + str(y))     #This code will not run at all