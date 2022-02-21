# Compilation of Codes
#Task 5
import requests

url = 'https://brickset.com/sets/year-2020'
r = requests.get(url)

print(r.text)

print("Source Code:")
print("\t*", r.status_code)

h = requests.head(url)
print("Header")
print("**********")

for x in h.headers:
    print("\t", x, ".", h.headers[x])
print("**********")

header = {
    'User-Agent' : 'Mobile'
}

url2 = 'https://httpbin.org/headers'

rh = requests.get(url2, headers=header)

print(rh.text)   

#Task 6
import scrapy

class NewSpider(scrapy.Spider):
   name = "new_spider"
   start_urls = ['http://brickset.com/sets/year-2020']
   def parse(self, response):
      #xpath_selector = '//img'
      css_selector='img'
      for  x in response.xpath(css_selector):
         newsel = '@src'
         yield {
            'Image Link': x.xpath(newsel).extract_first(),
         }
#To recurse next page
      Page_selector = '.next a ::attr(href)'
      next_page = response.css(Page_selector).extract_first()
      if next_page:
         yield scrapy.Request(
             response.urljoin(next_page),
             callback=self.parse
         )
            
#Task 7
import scrapy

class NewSpider(scrapy.Spider):
    name = "new spider"
    start_urls = ["https://brickset.com/sets/year-2020"]

    def parse(self, response):
        css_selector = "//img"
        for x in response.css(css_selector):
            newsel = "@src"
            yield {
                'Image Link': x.xpath(newsel).extract_first()
            }
            
      