# -*- coding: utf-8 -*-
import scrapy


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['www.renren.com']
    #重写spider类的start_requests()方法,去掉start_url
    def start_requests(self):
        url='http://www.renren.com/PLogin.do'
        #ForRequest()方法
        yield scrapy.ForRequest(url=url,
            fordata={
            'email':17865933895,
            'password':'zuobing19950520',
            },
            callback=self.parseHtml,
            )

    def parseHtml(self,response):
        with open('zuo.html','w') as f:
            f.write(response.text)