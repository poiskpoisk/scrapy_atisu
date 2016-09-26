# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.exceptions import DropItem

class AticldDuplicatesPipeline(object):
    def __init__(self):
        self.firmNames = set()
    def process_item(self, item, spider):
        if item['firmName'] in self.firmNames:
            raise DropItem("Duplicate item found: %s" % item['firmName'] )
        else:
            self.firmNames.add(item['firmName'])
        return item