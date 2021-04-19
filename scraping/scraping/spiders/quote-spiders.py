import scrapy

class QuoteSpider(scrapy.Spider):
	name = "Quotes"
	start_urls = ["https://bluelimelearning.github.io/my-fav-quotes/"]

	def parse(self, respnse):
		quotes = respnse.css("div.quotes")

		for quote in quotes:
			yield {
				"quote": quote.css("p.aquote::text").extract(),
				"author": quote.css("p.author::text").extract_first()
			}