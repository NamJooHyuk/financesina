#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_sinaDB = client[settings['MONGODB_DB']]
collect_sina_161209 = News_sinaDB[settings['MONGODB_COLLECTION']]