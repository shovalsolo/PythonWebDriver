# Example of a module file - a file that has a class or a method

def display(message, is_warning=False):
    if is_warning:
        print('Warning!!!')
    print(message)