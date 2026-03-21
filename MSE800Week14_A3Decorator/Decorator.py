
# ============================================
# Shows reusable function behavior with a decorator
# ============================================


# decorator function
def log_decorator(func):
    # this wrapper will run before and after function
    def wrapper(*args, **kwargs):
        # print function name and input values
        print(f"Calling {func.__name__} with {args}, {kwargs}")
        
        # run the original function
        result = func(*args, **kwargs)
        
        # print returned result
        print(f"{func.__name__} returned {result}")
        
        return result
    
    return wrapper


# ============================================
# function 1: add
# ============================================
@log_decorator
def add(a, b):
    # add two numbers
    return a + b


# ============================================
# function 2: multiply
# ============================================
@log_decorator
def multiply(a, b):
    # multiply two numbers
    return a * b


# ============================================
# main test code
# ============================================
if __name__ == "__main__":
    # test add function
    print("---- TEST ADD ----")
    add(3, 5)

    print()

    # test multiply function
    print("---- TEST MULTIPLY ----")
    multiply(2, 6)
