#Employee class with examples of inheritance between classes Employee and Developer
# isinstance - Checking if mgr_1 is an instance of class manager returning True or False
# issubclass - Checking if Developer is an sub class of class Employee

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


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self , first , last , pay , programming_language): #The Developer Class constructor and we are adding the parameters in the creation of the constructor
        super().__init__(first , last , pay)                #Initializing the variables from Employee class
        self.programming_language = programming_language    #Initializing the programming_language variable


class Manager(Employee):
    def __init__(self , first , last , pay , employees=None): #The Developer Class constructor and we are adding the parameters in the creation of the constructor
        super().__init__(first , last , pay)                #Initializing the variables from Employee class
        if employees is None:                               #If employees is empty
            self.employees = []                             #Create a empty list
        else:
            self.employees = employees                      #Initializing employees

    def add_employee(self , employee):                      #Add employee to manager list
        if employee not in self.employees:                  #
            self.employees.append(employee)                 #

    def remove_employee(self, employee):                    #Remove employee from manager list
        if employee in self.employees:                      #
            self.employees.remove(employee)                 #

    def print_employees(self):                              #Print employees from manager list
        for employee in self.employees:                     #
            print('--->', employee.fullname())              #


emp_1 = Employee('Kor','Mon',50000)                         #Creating an object(instance) of the class - we have to give all the params to create the object
emp_2 = Employee('For','Bon',60000)                         #Creating an object(instance) of the class - we have to give all the params to create the object
dev_1 = Developer('Lor','Bon',10000 , 'Java')               #Creating a Developer object that is inheriting from Employee
dev_2 = Developer('Por','Son',80000 , 'C#')                 #Creating a Developer object that is inheriting from Employee

mgr_1 = Manager('Or','Tal',10000 ,[dev_1])                  #Creating a Developer object that is inheriting from Employee
mgr_2 = Manager('Sho','Val',80000, [dev_2])                 #Creating a Developer object that is inheriting from Employee


if __name__=='__main__':                                                                #adding this line to be able to run tbe test from the ide and not from cmd
    print(dev_1.first, dev_1.last , dev_1.email , dev_1.pay, dev_1.programming_language)#
    print(dev_2.first, dev_2.last , dev_2.email , dev_2.pay, dev_2.programming_language)#

    mgr_1.add_employee(dev_2)                                                           #Adding dev_2 to the list of mgr_1
    print (mgr_1.first, mgr_1.last, mgr_1.email, mgr_1.pay , mgr_1.print_employees())   #Printing Manager 1 info
    mgr_1.remove_employee(dev_2)                                                        #Removing dev_2 from the list of mgr_1
    print (mgr_2.first, mgr_2.last, mgr_2.email, mgr_2.pay , mgr_2.print_employees())   #Printing Manager 2 info

    #print(help(Developer))                                                             #Showing the inheritance that Developer is getting from Employee

    print(isinstance(mgr_1, Manager),'is mgr_1 an instance of class manager')           #Checking if mgr_1 is an instance of class manager returning True or False
    print(isinstance (mgr_1, Developer),'is mgr_1 an instance of class Developer')      #Checking if mgr_1 is an instance of class manager returning True or False

    print (issubclass(Developer, Employee), 'is Developer an sub class of class Employee')#Checking if Developer is an sub class of class Employee
    print (issubclass(Manager, Employee),'is Manager an sub class of class Employee')  # Checking if Manager is an sub class of class Employee