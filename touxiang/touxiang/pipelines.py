# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo

class TouxiangPipeline(object):
    def process_item(self, item, spider):
        coon = pymongo.MongoClient("localhost",27017) # 连接mongo数据库
        db = coon.touxiang  # 创建数据库
        tabel = db.picture  # 创建表
        tabel.insert_one(dict(item))  # 插入一条数据,转化为字典
        return item

