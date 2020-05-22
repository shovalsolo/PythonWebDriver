# Example for numeric data types data types conversion
# timedelta is a method that can hold a delta of time and we can use it to do dates actions

from datetime import date, datetime, timedelta          #when importing can add more after the , from the same library 

today = datetime.now()

print('Today is : '+ str(today))                   #Will print the time now

one_day = timedelta(days=1)
yesterday = today - one_day
print('Yesturday was : ' +str(yesterday))


current_date = datetime.now()

print('Day: ' + str(current_date.day))

print('Month: ' + str(current_date.month))

print('Year: ' + str(current_date.year))

birthday = input('When is your birthday (dd/mm/yyyy)?')

birthday_date = datetime.strptime(birthday,'%d/%m/%Y')

print('Birthday: ' + str(birthday_date))


birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))


one_week = timedelta(weeks=1)
last_week = today - one_week
print('Last week was: ' +str(last_week))
