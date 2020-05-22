# Example of multiple conditions and/or

gpa = float(input('What was your GPA Average? '))
lowest_grade = float(input('What was your lowest grade? '))

# Same if
# 
# if gpa >= .85:
#     if lowest_grade >= .70:
#         print('You made the honor roll')


# Same if
# if gpa >= .85 and lowest_grade >= .70:
#     print('You made the honor roll')


if gpa >= .85 and lowest_grade >= .70:
    honor_roll = True
    print('You made the honor roll')
else:
    honor_roll = False
    print('You are not in the honor roll')
    
if honor_roll:
    print('You made the honor roll !!!!!')