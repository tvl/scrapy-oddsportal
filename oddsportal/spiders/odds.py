# -*- coding: utf-8 -*-
from scrapy import Spider, Request
#from scrapy.loader import ItemLoader
from oddsportal.items import Odd
from urllib.parse import parse_qs
from datetime import datetime, date, timedelta
import re

class OddsSpider(Spider):
    name = "odds"
    #allowed_domains = ["http://data.unogoal.me"]
    start_urls = ['file:///home/tvl/dev/scrapy-oddsportal/oddsportal/today.html',
            'file:///home/tvl/dev/scrapy-oddsportal/oddsportal/tomorrow.html']
    params = {
        "sport": "soccer",
        "page": "match",
        "id" : "2255155",
        "localization_id": "www"
    }

    def start_requests(self):
        #dates = ['2017-09-09', '2017-09-10', '2017-09-11']
        for u in self.start_urls:
            request = Request(url=u, callback=self.parse)
            #request.meta['proxy'] = 'http://127.0.0.1:8118'
            yield request

    def parse(self, response):
        items = []
        rows = response.xpath('//table[@class=" table-main"]//tr')
        if response.url.split('/')[-1] == 'today.html':
            odds_date = date.today()
        elif response.url.split('/')[-1] == 'tomorrow.html':
            odds_date = date.today() + timedelta(days=1)
        for row in rows:
            line = row.xpath('td//text()').extract()
            if len(line) == 0:
                area, competition = row.xpath('th/a/text()').extract()
                continue
            if line[-1] == '-':
                continue
            item = Odd()
            item['id'] = 0
            item['datetime'] = '{} {}:00'.format(odds_date,line[0])
            item['area'] = area
            item['competition'] = competition
            if line[1] == "'":
                item['datetime'] = odds_date
                item['home_team'], item['away_team'] = line[2].split(' - ')
                #item['score'] = line[-5]
            elif line[1] == '\xa0':
                item['home_team'], item['away_team'] = line[2].split(' - ')
                #item['score'] = line[-5]
            elif line[1][-3:] == ' - ':
                item['home_team'] = line[1][:-3]
                item['away_team'] = line[2]
                #item['score'] = line[-5]
            elif line[2][:3] == ' - ':
                item['home_team'] = line[1]
                item['away_team'] = line[2][3:]
                #item['score'] = line[-5]
            else:
                item['home_team'], item['away_team'] = line[1].split(' - ')
                #item['score'] = line[-5]
            item['home'] = line[-4]
            item['draw'] = line[-3]
            item['away'] = line[-2]
            item['odds'] = line[-1]
            item['updated'] = datetime.utcnow().isoformat(' ')
            yield item
            items.append(item)
        #return items
        #self.log('URL: {}'.format(response.url))


