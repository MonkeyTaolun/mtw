#!/usr/bin/env python
import json
import twitterutl as Utl
from dbConfig     import MongoConf
class MongoDataProc(object) :
  
  def __init__(self, term, dbconf):
    self.db = MongoConf(term, dbconf)
    self.count = 0
  def process(self, tweets) :
    self.count = self.count + 1
    print self.count
   # for twi in tweets:
    tweet = json.loads(tweets)
    #print tweet
    twi = Utl.processTweetStream(tweet)
    print "Shittty"
    #print twi['id']
    self.db.insert(json.loads(twi))
   #   self.db.insert(Utl.procssTweetJson(tweet)



if __name__ == '__main__' :
  print "helloworld"
