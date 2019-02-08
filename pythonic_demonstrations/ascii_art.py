import pyfiglet
from termcolor import colored

msg = input ("What would you like to print?")
color = input ("Which color would you like text to be printed")
#valid colors: red, green, yellow, magenta, cyan, white
if color not in valid_colors:
    color = "green"


ascii_art = pyfiglet.figlet_format(msg)
colored_ascii = colored(ascii_art, color=color)
print(ascii_art)


