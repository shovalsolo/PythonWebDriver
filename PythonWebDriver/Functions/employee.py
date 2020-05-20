#An employee class with the following methods
# email , fullname , apply_raise , monthly_schedule

import requests

class Employee:
    """A sample Employee class"""

    raise_amt = 1.05

    def __init__(self, first, last, pay):                       #A method to initialize the parameters getting 3 parameters
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def email(self):                                            #A method that is getting first and last name and returning an email address
        return '{}.{}@email.com'.format(self.first, self.last)

    @property                                                   #A method that is getting first and last name and returning full name
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):                                      #A method that is calculating the raise getting pay and raise amount and applying a rise of 5% on the salary
        self.pay = int(self.pay * self.raise_amt)

    def monthly_schedule(self, month):                          #
        response = requests.get(f'http://company.com/{self.last}/{month}')
        if response.ok:
            return response.text
        else:
            return 'Bad Response!'

