#!/usr/bin/env python

from twitterSearch  import  SearchCrawler
from twitterCrawler import  TwitterCrawler 
from dbConfig       import  MongoConf
import json

class TweetCrawler(object):
  def __init__(self, term, twiconf, dbconf):
    self.searchCrawler  = SearchCrawler(term, 2000, 3, 100)
    self.twitterCrawler = TwitterCrawler(twiconf, 5)
    self.db             = MongoConf(term, dbconf)

  def crawl(self):
    searchResult = self.searchCrawler.crawl()
    idset = set()
    tagset = set()
    for tweet in searchResult:
      twi = json.loads(tweet)
      idset.add(twi['uid'])
      if(None != twi['tid']):
        idset.add(twi['tid'])
      if(None != twi['tag']):
        tagset.add(twi['tag'])
      print "get tweet %s from search" %(twi['id'])
      self.db.insert(twi)
    
    self.deepCrawl(idset, 0)
    self.tagCrawl(tagset)
  def deepCrawl(self, idset, depth):
    if(depth > 3): 
      return
    myset = set()
    for uid in idset:
      tweets  = self.twitterCrawler.getByUserID(uid)
      for tweet in tweets['usertweets']:
        twi = json.loads(tweet)
        print "get tweet %s from deepCrawl" %(twi['id'])
        self.db.insert(twi)
      for tweet in tweets['friendstweets']:
        twi = json.loads(tweet)
        if(None != twi['tid']):
          myset.add(twi['tid'])
        print "get tweet %s from deepCrawl" %(twi['id'])
        myset.add(twi['uid'])
        self.db.insert(twi)
    
    self.deepCrawl(myset, depth + 1)
  def tagCrawl(self, tagset):
    for tag in tagset:
      tagcrawler  = SearchCrawler(tag, 100, 24, 20)
      tagtweets = tagcrawler.crawl()
      for tweet in tagtweets:
        twi = json.loads(tweet)
        print "get tweet %s hashtag" %(twi['id'])
        self.db.insert(twi)


if __name__ == '__main__':
  
  crawler = TweetCrawler('HIV', 'tweetconf.json', 'db.json')
  crawler.crawl()
