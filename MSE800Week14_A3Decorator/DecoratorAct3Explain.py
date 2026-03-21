# simple decorator
def my_decorator(func):
    def wrapper(*args, **kwargs):
        # show all inputs
        print("args:", args)
        print("kwargs:", kwargs)
        
        # call original function
        return func(*args, **kwargs)
    
    return wrapper


# function 1 (normal values)
@my_decorator
def add(a, b):
    return a + b


# function 2 (named values)
@my_decorator
def greet(name="Guest"):
    return f"Hello {name}"


# test
print(add(2, 3))                 # args example
print(greet(name="Ben Reves"))        # kwargs example


# Decorator explanation:
# *args → catch all normal values   ---example: add(2,3) → args = (2,3) 
# **kwargs → catch all named values  example: name="Ben Reves" → kwargs = {'name':'Ben Reves'}
# decorator can wrap ANY function