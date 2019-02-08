def display_names (first, second):
    print(f"{first} say hello to {second}")

names = {"first": "braxton", "second": "Hutchins"}

#dislpay_names(names) # error
display_names(**names)

#single star unpacks tuples and lists, ** unpacks dictionaries....

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a+b*c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55, name="Tony")
add_and_multiply_numbers(**data)