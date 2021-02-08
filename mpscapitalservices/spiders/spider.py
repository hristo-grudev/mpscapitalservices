import scrapy
from scrapy.exceptions import CloseSpider

from scrapy.loader import ItemLoader
from ..items import MpscapitalservicesItem
from itemloaders.processors import TakeFirst


class MpscapitalservicesSpider(scrapy.Spider):
	name = 'mpscapitalservices'
	start_urls = ['http://www.mpscapitalservices.it/AreaMedia/News/Archivio/default.htm']

	def parse(self, response):
		years = response.xpath('//select[@name="ddlAnno"]/option/text()').getall()
		months = response.xpath('//select[@name="ddlMese"]/option/text()').getall()

		for year in years:
			for month in months:
				link = f'http://www.mpscapitalservices.it/AreaMedia/News/Archivio/default.htm?Mese={month}&Anno={year}'
				yield response.follow(link, self.parse_month)

	def parse_month(self, response):
		article_links = response.xpath('//a[@class="linkGrigio"]/@href')
		yield from response.follow_all(article_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="contenitoreCentro"]//p//text()|//div[@id="phTesto"]//text()').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@id="spanData"]/text()').get()

		item = ItemLoader(item=MpscapitalservicesItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		item.add_value('date', date)

		return item.load_item()
