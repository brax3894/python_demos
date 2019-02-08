from pyfiglet import figlet_format
from termcolor import colored


#valid colors: red, green, yellow, magenta, cyan, white
def print_art(msg, color):
    valid_colors = ("red", "green", "yellow", "magenta", "cyan", "white")
    if color not in valid_colors:
        color = "green"
    ascii_art = figlet_format(msg)
    colored_ascii = colored(ascii_art, color=color)
    print (colored_ascii)

msg = input ("What would you like to print?")
color = input ("Which color would you like text to be printed")

print_art(msg, color)
