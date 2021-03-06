import scrapy

# In place of start_urls array attribute
urls = [
	"http://www.shopclues.com/mobiles-featured-store-4g-smartphone.html/",
	]

class ShopcluesSpider(scrapy.Spider):
   name = "shopclues"
   allowed_domains = ["http://www.shopclues.com"]
   custom_settings = {
       "FEED_URI" : "tmp/shopclues/shopclues.csv"
   }

   def start_requests(self):
       for url in urls:
          yield scrapy.Request(url, scrapy.parse)

   def parse(self, response):
       titles = response.css("img::attr(title)").extract()
       images = response.css("img::attr(data-img)").extract()
       prices = response.css(".p_price::text").extract()
       discounts = response.css(".prd_discount::text").extract()

       for item in zip(titles, prices, images, discounts):
           scraped_info = {
               "title": item[0],
               "price": item[1],
               "image_urls": [item[2]], #Set"s the url for scrapy to download images
               "discount" : item[3]
           }

           yield scraped_info