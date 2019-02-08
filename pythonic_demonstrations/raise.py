def colorize (text, color):
    colors= ("yellow", "red", "blue", "teal", "purple")
    if type(text) is not str:
        raise TypeError("color must be instance of str")
    if type(text) is not str:
        raise ValueError("text must be instance of str")
    if color not in colors:
        raise ValueError("color is invalid color")
    print (f"printed {text} in {color}")
