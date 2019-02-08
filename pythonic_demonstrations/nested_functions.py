from random import choice
#this is my nested function demo

def greet(person):
    def get_mood():
        msg = choice(("hello there ", "go away ", "I love you "))
        return msg
    result = get_mood() + person
    return result

print(greet("Braxton"))