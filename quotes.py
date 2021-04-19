from urllib.request import urlopen
from bs4 import BeautifulSoup as bs

address = "https://bluelimelearning.github.io/my-fav-quotes/"
urlClient = urlopen(address)
content = urlClient.read()
urlClient.close()

soup = bs(content, "html.parser")

quotes = soup.findAll("div", {"class": "quotes"})
for quote in quotes:
	favQuotes = quote.findAll("p", {"class": "aquote"})
	favQuote = favQuotes[0].text.strip()
	favAuthors = quote.findAll("p", {"class": "author"})
	favAuthor = favAuthors[0].text.strip()

	print(favQuote)
	print(favAuthor)
	print("\n")