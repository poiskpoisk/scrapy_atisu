# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

class AticldItem(Item):
    firmName = Field()  # Имя компании или ФИО физлица
    nickName = Field()  # Ник на форуме
    inn      = Field()  # ИНН
    role     = Field()  # роль - Грузоперевозчик, Грузоотправитель и тп
    city     = Field()  # город в котором работает компания
    tel      = Field()  # телефон
    icq      = Field()  # icq
    skype    = Field()  # скайп
