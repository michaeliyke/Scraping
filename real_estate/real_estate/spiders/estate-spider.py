import scrapy

class RealEstate(scrapy.Spider):
	def parse(self, response): 
		item_loader = ItemLoader(item=RealEstateItem(), response=response) 
		item_loader.default_input_processor = MapCompose(remove_tags) 
		item_loader.default_output_processor = TakeFirst() 
		item_loader.add_value("url", response.url) 
		item_loader.add_xpath("listing_type", "") 
		item_loader.add_css("price", "") 
		item_loader.add_css("price", "") 
		item_loader.add_xpath("house_size", "") 
		item_loader.add_css("city", "") 
		item_loader.add_xpath("year_built","") 
		return item_loader.load_item() 