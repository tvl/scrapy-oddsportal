# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field



class UnogoalItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Match(Item):
    id = Field()
    datetime = Field()
    competition_id = Field()
    fifa_id = Field()
    home_team_id = Field()
    home_team = Field()
    away_team_id = Field()
    away_team = Field()
    home = Field()
    draw = Field()
    away = Field()
    hts = Field()
    fts = Field()
    updated = Field()

class Odd(Item):
    id = Field()
    datetime = Field()
    area = Field()
    competition = Field()
    #fifa_id = Field()
    #home_team_id = Field()
    home_team = Field()
    #away_team_id = Field()
    away_team = Field()
    home = Field()
    draw = Field()
    away = Field()
    #hts = Field()
    #score = Field()
    #fts = Field()
    odds = Field()
    updated = Field()


