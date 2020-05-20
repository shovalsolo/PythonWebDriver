
def add(x, y):              # A function that is getting 2 params adding them and returning the result
    """Add Function"""
    return x + y


def subtract(x, y):         # A function that is getting 2 params Subtracting them and returning the result
    """Subtract Function"""
    return x - y


def multiply(x, y):         # A function that is getting 2 params Multiplying them and returning the result
    """Multiply Function"""
    return x * y


def divide(x, y):         # A function that is getting 2 params Dividing them and returning the result
    """Divide Function"""
    if y == 0:
        raise ValueError('Can not divide by zero!')
    return x / y

#print(add(10,5))
#print(subtract(10,5))
#print(multiply(10,5))
#print(divide(10,5))