#!/usr/bin/env python

from tweetCrawler import TweetCrawler


crawler1 = TweetCrawler('AIDS', 'tweetconf.json', 'aids.json')

crawler2 = TweetCrawler('Malaria', 'tweetconf.json', 'malaria.json')

crawler3 = TweetCrawler('FLU', 'tweetconf.json', 'flu.json')


crawler1.crawl()
print "getAIDS"

crawler2.crawl()

crawler3.crawl()
