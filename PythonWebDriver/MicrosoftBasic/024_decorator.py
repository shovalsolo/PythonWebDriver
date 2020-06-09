# This is an example of Decorator call

def logger(func):                       #logger method
    def wrapper():                      
        print('Logging execution')      
        func()                          #will call the sample method
        print('Done logging')           
    return wrapper                      

@logger                                 #Decorator logger calling the method 
def sample():                           #method with a print
    print('-- Inside sample function')  
    
sample()                                #Calling the sample method