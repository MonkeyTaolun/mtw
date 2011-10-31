#!/usr/bin/env python

from tweetCrawler import TweetCrawler

queries   = [ 'cholera',    'diabetes',   'mosquito net', 
              'HIV',        'Plasmodium', 'fever', 
              'shivering',  'vomiting',   'arthralgia', 
              'parasites',  'drought',    'famine', 
              'erosion',    'hunger',     'flood', 
              'food crisis','harvesting', 'starvation', 
              'farming',    'drought',    'famine',
              'erosion',    'hunger',     'flood',
              'AIDS',       'Food crisis','harvesting',
              'starvation', 'farming',    'malaria',
              'flu']

for query in queries:
  crawler = TweetCrawler(query,'tweetconf.json', 'db.json')
  crawler.crawl()

