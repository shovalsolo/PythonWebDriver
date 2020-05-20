#Employee class with a constrictor to Initialize the params
#function that is concatenating the first and last name and returning
# Employee. is used to call class variables like
# emp_1. is used to call the object that is created from the class

class Employee:
    num_of_employees = 0                                    #Will count the amount of the employees created
    raise_amount = 1.04                                     #A class variable raise_amount of 4%

    def __init__(self , first , last , pay):                #The Class constructor and we are adding the parameters in the creation of the constructor
        self.first = first                                  #Initializing the first name param
        self.last = last                                    #Initializing params
        self.pay = pay                                      #Initializing params
        self.email = first + '.' + last + '@Company.com'    #Initializing params
        Employee.num_of_employees += 1                      #Adding 1 to num_of_employees for every employee created using Employee because num_of_employees is a class variable

    def fullname(self):                                     #A method the is concatenating the first and last name and returning
        return '{} {}'.format (self.first, self.last)       #R returning first and last name after concatenating

    def applay_raise(self):                                 #A method that is applying a raise
        self.pay = int(self.pay * self.raise_amount)        #Multiplaying the pay by raise_amount adding 4% to the pay of the employee

    @classmethod                                            #classmethod is a method that is receiving the class as cls to the method
    def set_raise_amount(cls,amount):                       #The method is getting the class as cls and amount
        cls.raise_amount = amount                           #Setting the Raise amount that is a class variable to amount from user


emp_1 = Employee('Kor','Mon',50000)                         #Creating an object(instance) of the class - we have to give all the params to create the object
emp_2 = Employee('For','Bon',60000)                         #Creating an object(instance) of the class - we have to give all the params to create the object
print('raise_amount = ',Employee.raise_amount)              #Printing raise_amount
print('Employees created = ',Employee.num_of_employees)     #Printing num_of_employees

if __name__=='__main__':                                    #adding this line to be able to run tbe test from the ide and not from cmd
    print ('\n','Employee 1')                               #Will go down 1 row
    print (emp_1)
    print (emp_1.fullname())                                #Printing the function return the first and last
    print (emp_1.first)                                     #Printing first name
    print (emp_1.last)                                      #Printing last name
    print (emp_1.email)                                     #Printing email
    print (emp_1.pay , 'before raise')                      #Printing pay before raise
    emp_1.applay_raise()                                    #Running the applay_raise method
    print (emp_1.pay , 'after raise')                       #Printing the pay after the raise to see the method applay_raise effect
    print('{} {}'.format(emp_1.first,emp_1.last))           #Will concatenate the first and last name to one string

    print ('\n','Employee 2')                               #Will go down 1 row
    print(emp_2.fullname())                                 #Printing the function return the first and last
    print (emp_2)
    print (emp_2.first)
    print (emp_2.last)
    print (emp_2.email)
    print (emp_2.pay)
    print ('{} {}'.format (emp_2.first, emp_2.last))        #Will concatenate the first and last name to one string
    print ('\n')

    print ('\n', 'Employee 1 attributes')
    print (emp_1.__dict__)

    print ('\n', 'Employee 2 attributes')
    print (emp_2.__dict__)

    print ('\n', 'Employee class attributes')
    print (Employee.__dict__)

    print ('\n')
    Employee.set_raise_amount(1.07)                         # Using the @classmethod method to update the raise_amount
    print ('raise_amount = ', Employee.raise_amount)        # Printing raise_amount after update
