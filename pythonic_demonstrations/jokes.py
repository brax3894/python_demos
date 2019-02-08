import requests
from random import choice
import pyfiglet
from termcolor import colored
header = pyfiglet.figlet_format("DADBOT 3K")
header = colored(header, color="green")
print (header)
user_search = input ("What would you like to search for?")
url = "https://icanhazdadjoke.com/search"
res = requests.get(
    url,
    headers={"Accept": "application/json"},
    params={"term":user_search}
).json()

num_jokes = len(res["results"])
results = res["results"]
if num_jokes > 1:
    print (f"there are {num_jokes} jokes about {user_search}. Here's one: ")
    choice(results)
elif num_jokes == 1:
    print(f"there is one joke about {user_search}")
    print(res["results"][0])
else:
    print ("there are no jokes for your search")