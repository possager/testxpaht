#_*_coding:utf-8_*_
import scrapy
import re
import time

class testxpath(scrapy.Spider):
    name = 'baidu'
    urls=['http://sn.newssc.org/2016fc/']
    headers={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}

    def start_requests(self):
        for url in self.urls:
            yield scrapy.Request(url=url,headers=self.headers)

    def parse(self, response):
        print response.body

        print response.xpath('/html/body/div[9]/table/tbody/tr/td[1]/div/table[2]/tbody/tr[3]/td/div/table/tbody/tr[1]/td/table/tbody/tr[2]/td/table/tbody/tr/td[2]/table/tbody/tr[1]/td').extract()#说明了这里的[num]中的num是需要-1的,第二个就是1,第一个是0