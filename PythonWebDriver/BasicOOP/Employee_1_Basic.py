#Basic class , how to create instances of the class , how to add new parameters to the class and print them


class Employee:
    pass                                #pass is a temporary command to skip this code

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "Tom"
emp_1.last = "Cor"
emp_1.email = "Tom.Cor@company.com"
emp_1.pay = 50000

emp_2.first = "Lon"
emp_2.last = "Bon"
emp_2.email = "Lon.Bon@company.com"
emp_2.pay = 60000


if __name__=='__main__':                 #adding this line to be able to run tbe test from the ide and not from cmd
    print ('\n')
    print (emp_1)
    print(emp_1.first)
    print (emp_1.last)
    print (emp_1.email)
    print (emp_1.pay)

    print ('\n')
    print(emp_2)
    print (emp_2.first)
    print (emp_2.last)
    print (emp_2.email)
    print (emp_2.pay)




