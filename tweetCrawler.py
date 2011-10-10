#!/usr/bin/env python

from twitterSearch  import  SearchCrawler
from twitterCrawler import  TwitterCrawler 
from dbConfig       import  MongoConf
import json

class TweetCrawler(object):
  def __init__(self, term, twiconf, dbconf):
    self.searchCrawler  = SearchCrawler(term)
    self.twitterCrawler = TwitterCrawler(twiconf)
    self.db             = MongoConf(dbconf)

  def crawl(self):
    searchResult = self.searchCrawler.crawl()
    idset = set()
    for tweet in searchResult:
      twi = json.loads(tweet)
      idset.add(twi['uid'])
      if(None != twi['tid']):
        idset.add(twi['tid'])
      self.db.insert(twi)
    
    self.deepCrawl(idset, 0);

  def deepCrawl(self, idset, depth):
    if(depth > 3): 
      return
    myset = set()
    for uid in idset:
      tweets  = self.twitterCrawler.getByUserID(uid)
      for tweet in tweets['usertweets']:
        twi = json.loads(tweet)
        self.db.insert(twi)
      for tweet in tweets['friendstweets']:
        twi = json.loads(tweet)
        if(None != twi['tid']):
          myset.add(twi['tid'])

        myset.add(twi['uid'])
        self.db.insert(twi)
    
    self.deepCrawl(myset, depth + 1)
  
