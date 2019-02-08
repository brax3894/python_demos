def shout(fn):
    def wrapper(name):
        return fn(name).upper()
    return wrapper()

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like to place an order for {main}, with a side of {side} please."

print(greet("todd"))
print(order("burger", "fries"))

###############################################

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper()

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like to place an order for {main}, with a side of {side} please."

print(greet("todd"))
print(order("burger", "fries"))