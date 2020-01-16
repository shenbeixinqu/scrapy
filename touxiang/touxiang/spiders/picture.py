# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from touxiang.items import TouxiangItem

class PictureSpider(scrapy.Spider):
    name = 'picture'
    # allowed_domains = ['www.xxx.com']
    def start_requests(self):
        url = "https://www.woyaogexing.com/touxiang/"
        yield Request(url)

    def parse(self, response):
        div_list = response.xpath("//div[@class='list-left z']/div[2]/div")
        for i in div_list:
            name = i.xpath('./a/text()').extract_first()  # 变量名 要与items.py中实例化的变量名一样
            img_url = i.xpath('./a/img/@src').extract_first()
            lianjie_url = i.xpath('./a/@href').extract_first()
            items = TouxiangItem()  # 实例化items
            items['name'] = name  # 将实例化的字段存进字典中
            items['img_url'] = img_url
            items['lianjie_url'] = lianjie_url
            yield items  # 发送给管道