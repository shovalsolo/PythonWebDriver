# Example for numeric data types data types conversion
pi = 3.14159
print(pi1)


first_num = 6
second_num = 2
print(first_num + second_num)
print(first_num * second_num)
print(first_num ** second_num)                  # ** is exponent

days_in_feb = 28
print('Days in February'+ str(days_in_feb))     # converting the int to string

first_num = input('Enter first number: ')
second_num = input('Enter second number: ')

print(first_num + second_num)                   # will connect the strings without converting

print(int(first_num) + int(second_num))         # will connect the strings converting but will convert to int before

print(float(first_num) + float(second_num))     # will connect the strings converting but will convert to float before