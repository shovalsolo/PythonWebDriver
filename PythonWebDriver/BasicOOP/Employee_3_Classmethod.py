#Employee class with examples of @classmethod
#@classmethod is a method That is getting the class as cls
#@classmethod as an alternative constrictor - to initialize the class variables

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

    @classmethod
    def from_string(cls, employee_string):                  #A method that is getting a string , splitting and returning it to parameters and saving to cls - alternative constructor
        first , last , pay = employee_string.split('-')     #Spliting the string for every variable
        return cls(first , last , pay )                     #Returning the class variables


if __name__=='__main__':                                    #adding this line to be able to run tbe test from the ide and not from cmd
    emp_str_1 = 'John-Doe-70000'                            #Creating a string to create a new employee
    new_emp_1 = Employee.from_string(emp_str_1)             #Sending the string to the method to split and insert to the cls
    print(new_emp_1.first, new_emp_1.last ,new_emp_1.pay , new_emp_1.email) # printing the employee info