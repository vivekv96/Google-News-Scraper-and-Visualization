from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector

class MySpider(Spider):
    name = "toi"
    allowed_domains = ["http://timesofindia.indiatimes.com/"]
    start_urls = ["http://timesofindia.indiatimes.com/rssfeedstopstories.cms"]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        titles = hxs.xpath("title")
        items = []
        for titles in titles:
            item["title"] = titles.select("a/text()").extract()
            item["link"] = titles.select("a/@href").extract()
            items.append(item)
        return items