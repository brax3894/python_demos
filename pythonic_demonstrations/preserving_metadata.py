#functools helps us preserve metadata in our wrapped functions
from functools import wraps
def log_function_data(fn):
    #@wraps calls down to wrapper function add, and then plugs in the data relative to its wrapper call tag
    @wraps(fn)
    def wrapper(*args, **kwargs):
        """I AM WRAPPER FUNCTION"""
        print(f"you are about to call {fn.__name__}")
        print(f"Here's the documentation: {fn.__doc__}")
        return fn(*args, **kwargs)
    return wrapper

#wrapper call tag
@log_function_data

def add(x,y):
    """Adds two numbers together."""
    return x + y

print(add.__doc__)
print(add.__name__)
help(add)
