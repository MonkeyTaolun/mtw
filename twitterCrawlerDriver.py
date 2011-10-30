#!/usr/bin/env python

from tweetCrawler import TweetCrawler
  drought
  famine  erosion
  hunger  flood
  Food Crisis harvesting
  starvation  farming
queries   = ['cholera', 'diabetes', 'mosquito net', 'HIV', 'Plasmodium', 'fever', 'shivering', 'vomiting', 'arthralgia', 'parasites', 'drought', 'famine', 'erosion', 'hunger', 'flood', 'food crisis', 'harvesting', 'starvation', 'farming']


crawler1  = TweetCrawler('AIDS', 'tweetconf.json', 'aids.json')

crawler2  = TweetCrawler('Malaria', 'tweetconf.json', 'malaria.json')

crawler3  = TweetCrawler('FLU', 'tweetconf.json', 'flu.json')


crawler1.crawl()

crawler2.crawl()

crawler3.crawl()

