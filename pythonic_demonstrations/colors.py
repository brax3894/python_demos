def fav_colors(**kwargs):
    for person, color in kwargs.items():
        print(f"{person}'s favorite color is {color}")
fav_colors(braxton="green", sean = "blue", amy="pink")