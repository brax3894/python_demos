def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print ("do not divide by zero")


print (divide(1,2))
print (divide(1,0))