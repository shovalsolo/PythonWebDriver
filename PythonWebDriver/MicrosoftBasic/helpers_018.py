# Example of a module file - a file that has a class or a method
# This file is a service for 018_using_module

from pip._vendor.colorama import init, Fore

def display(message, is_warning=False):
    if is_warning:
        print(Fore.RED + 'Warning!!!')
    else:
        print(Fore.BLUE + message)