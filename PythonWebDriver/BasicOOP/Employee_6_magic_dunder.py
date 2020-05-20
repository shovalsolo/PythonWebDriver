#Employee class with examples dunder methods
#Dunder - is the __init__ , __repr__ , __str__ type of methods
#repr - methods that are called and we can control how we display the variables (fist , last , pay)
#str - methods that are called and we can control how we display the methods data (fullname and emal)

import datetime

class Employee:
    num_of_employees = 0                                    #Will count the amount of the employees created
    raise_amount = 1.04                                     #A class variable raise_amount of 4%
    my_date = datetime.date(2020, 1, 16)                    #Holding a day we want to check for a work day

    def __init__(self , first , last , pay):                #The Employee Class constructor and we are adding the parameters in the creation of the constructor
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

    @staticmethod                                           #Do not work on the instance or the class
    def is_workday(day):                                    #A method that is returning true or false for if it is a work week (Monday = 0 ,Tuesday = 1 , Wednesday = 2 , Thursday = 3 , Friday = 4 , Saturday = 5 , Sunday = 6 )
        if day.weekday() == 5 or day.weekday() == 6:        #checking if weekday is equal to 5 or 6 if so
            return False                                    #Returninng false
        return True                                         #Other returning True

    @property
    def __repr__(self):
        return  "Employee"('{}','{}','{}').format(self.first , self.last , self.pay)

    def __str__(self):
      return ('{} - {}').format(self.fullname(),self.email)

    def __add__(self, other):
        return self.pay + other.pay



emp_1 = Employee('Kor','Mon',50000)                         #Creating an object(instance) of the class - we have to give all the params to create the object
emp_2 = Employee('For','Bon',60000)                         #Creating an object(instance) of the class - we have to give all the params to create the object

if __name__=='__main__':                                                                #adding this line to be able to run tbe test from the ide and not from cmd

    print('\n')
    print(emp_1)
    print('from repr method __repr__: ',repr(emp_1))
    print('from str method __str__: ',str(emp_2))
    print('add dunder method __add__: adding the pay of emp_1 and emp_2 : ' , emp_1 + emp_2)