from scrapy.selector import Selector
from scrapy.http import HtmlResponse
response = HtmlResponse(url='https://10minutemail.net/', body=body)
Selector(response=response).xpath('//span/text()').get()
print(Selector)