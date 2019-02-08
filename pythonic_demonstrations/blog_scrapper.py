import requests
from bs4 import BeautifulSoup
from csv imoprt writer

#get the html response
response = requests.get("https://www.rithmschool.com/blog")
#gives the response to beutifulsoul, parses it into workable python, saves the parsed info in a variable
soup = BeautifulSoup(response.text, "html.parser")
#seaches the new variable for every tag called "article"
articles = soup.find_all("article")

#prints new parsed information
#print(articles)
##############

#scans articles for the <a> tag, pulls text from it,
# the variable title is to be saved to a CSV, prints the href
with open("blog_data.csv", "w") as csv_file:
    csv_writer = writer(csv_file)
    csv_writer.writerow(["title", "url", "date"])
    for article in articles:
        a_tag = article.find("a")
        href = a_tag["href"]
        title = a_tag.get_text()
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, href, date])
    #title = (article.find("a").get_text())
    #print(article.find("a")['href'])
    #print(a_tag['href'])

