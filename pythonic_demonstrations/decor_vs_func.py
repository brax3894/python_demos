#this is an example of a decorator as defined in a function
#vvvvv this is the decorator vvvvvv
def be_polite(fn):
    def wrapper():
        print("how awesome to meet you")
        fn()
        print("Have a great day")
    return wrapper

#vvv this is to be decorated
def greet():
    print("Whats new, my name is Braxton")
#another example
def rage ():
    print("I hate you! Go away!!")


#function with decorator##

def be_polite(fn):
    def wrapper():
        print("how awesome to meet you")
        fn()
        print("Have a great day")
    return wrapper

#vvv this is to be decorated
@be_polite
def greet():
    print("Whats new, my name is Braxton")
#another example
@be_polite
def rage ():
    print("I hate you! Go away!!")

#decoration in action

greet()

rage()