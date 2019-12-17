# -*- coding: utf-8 -*-
import scrapy
import re
from employment.items import EmploymentItem


class EmploySpider(scrapy.Spider):
    name = 'employ'
    allowed_domains = ['51job.com']
    start_urls= [
        'http://search.51job.com/list/030200,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
    ]

    def parse(self, response):
        '''
        :param response:
        :return:
        '''
        for item in response.css('div.dw_table div.el'):
            yield {
                "title": item.css('p a::attr(title)').extract_first(),
                "link": item.css('p a::attr(href)').extract_first(),
                "company": item.css('span.t2 a::attr(title)').extract_first(),
                "city": item.css('span.t3 ::text').extract_first(),
                "salary": item.css('span.t4 ::text').extract_first(),
                "createTime": item.css('span.t5 ::text').extract_first()
            }

        next_page = response.css('div.p_in ul li.bk a::attr(href)').extract()
        if next_page is not None:
            if len(next_page) > 1:
                yield response.follow(next_page[1], callback=self.parse)
            else:
                yield response.follow(next_page[0], callback=self.parse)