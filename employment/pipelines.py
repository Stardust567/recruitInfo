# -*- coding: utf-8 -*-
from scrapy.exceptions import DropItem
import json
import codecs
import logging
import pymongo
from scrapy.conf import settings


class EmploymentPipeline(object):

    def process_item(self, item, spider):
        title = item['title']
        if title:
            if title is "职位名":
                raise DropItem('title information was missing')
        else:
            raise DropItem('title information was missing')
        company = item['company']
        if company:
            if company is "公司名":
                raise DropItem('company information was missing')
        else:
            raise DropItem('company information was missing')
        salary = item['salary']
        if salary:
            if salary is "薪资":
                raise DropItem('Salary information was missing')
        else:
            raise DropItem('Salary information was missing')
        city = item['city']
        if city:
            if city is "工作地点":
                raise DropItem('city information was missing')
        else:
            raise DropItem('city information was missing')
        createTime = item['createTime']
        if createTime:
            if createTime is "发布时间":
                raise DropItem('createTime information was missing')
        else:
            raise DropItem('createTime information was missing')
        link = item['link']
        if link:
            return item
        else:
            raise DropItem('link information was missing')

    def spider_closed(self, spider):
        self.file.close()

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = codecs.open('data_utf8.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line)
        return item

    def spider_closed(self, spider):
        self.file.close()

class MongoPipeline(object):

    def __init__(self):
        # 链接数据库
        client = pymongo.MongoClient(host=settings['MONGO_HOST'], port=settings['MONGO_PORT'])
        self.db = client[settings['MONGO_DB']]  # 获得数据库的句柄
        self.coll = self.db[settings['MONGO_COLL']]  # 获得collection的句柄
        # 数据库登录需要帐号密码的话
        # self.db.authenticate(settings['MONGO_USER'], settings['MONGO_PSW'])
 
    def process_item(self, item, spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.coll.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写