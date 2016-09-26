# -*- coding: utf-8 -*-
__author__ = 'AMA'

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import logging

# create logger with 'SPIDER'
logger = logging.getLogger('SPIDER')
logger.setLevel(logging.INFO)

from aticld.items import AticldItem

class AtisuSpider( CrawlSpider ):

    name = "aticld2"
    allowed_domains = ["ati.su", "autotrust.info"]
    start_urls = ["http://ati.su/Forum/Default.aspx"]

    rules = (
        Rule(LinkExtractor( allow=('ShowForum\.aspx',) , deny=('LastMessage','Login\.aspx','News\.aspx',) )),
        Rule(LinkExtractor( allow=('Topic\.aspx',)     , deny=('LastMessage','Login\.aspx','News\.aspx',) ),
             callback='parse_forum', follow=True),
    )

    def parse_forum(self, response ):
        for prefix in range(3,23):
            prefix="%02d"%prefix
            item = AticldItem()
            firmName = '//a[contains(@id,'   +'"ctl'+prefix+'_FirmHyperLink")]//@title'
            nickName = '//a[contains(@id,'   +'"ctl'+prefix+'_chlkLocalUser")]//text()'
            inn      = '//span[contains(@id,'+'"ctl'+prefix+'_FirmHyperLink1_Label4")]//text()'
            role     = '//span[contains(@id,'+'"ctl'+prefix+'_FirmHyperLink1_lblProfile")]//text()'
            city     = '//span[contains(@id,'+'"ctl'+prefix+'_FirmHyperLink1_lblCity")]//text()'
            tel      = '//a[contains(@id,'   +'"ctl'+prefix+'_chlkLocalUser_cellHyp")]//@title'
            icq      = '//a[contains(@id,'   +'"ctl'+prefix+'_chlkLocalUser_icqHyp")]//@title'
            skype    = '//a[contains(@id,'   +'"ctl'+prefix+'_chlkLocalUser_hlkSkype")]//@alt'

            item['firmName']=response.xpath(firmName).extract_first()
            item['nickName']=response.xpath(nickName).extract_first()
            item['inn']     =response.xpath(inn).extract_first()
            try: item['inn']=item['inn'][5:-1:]
            except: pass
            item['role']    =response.xpath(role).extract_first()
            item['city']    =response.xpath(city).extract_first()
            item['tel']     =response.xpath(tel).extract_first()
            item['icq']     =response.xpath(icq).extract_first()
            item['skype']   =response.xpath(skype).extract_first()

            if item['firmName'] is not None :
                logger.info( u'-%s- Фирма %s Имя %s ИНН %s Роль %s' %(prefix, item['firmName'], item['nickName'],
                                                                  item['inn'], item['role'] ))
                logger.info( u'Город %s Tel %s ICQ %s Skype %s' %(item['city'],item['tel'],item['icq'],item['skype']) )
                yield item











