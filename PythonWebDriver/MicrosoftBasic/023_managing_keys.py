# This is an example of how to manage keys using .env file
# need to import dotenv with:  pip install -U python-dotenv

from dotenv import load_dotenv

load_dotenv()
import os

user = os.getenv('USER')
password = os.getenv('PASSWORD')

print()
print(user)
print()
print(password)