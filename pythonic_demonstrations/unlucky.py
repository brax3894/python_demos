number_range = range (1,21)
for num in number_range:
    if num == 4 or num == 13:
        print(f"{num} is Unlucky!")
    elif num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


        # for num in number_range:
#     if num in number_range ==4 or num in number_range ==13:
#         print("Unlucky!")
#     elif num in number_range %2 == 0:
#         print("even")
