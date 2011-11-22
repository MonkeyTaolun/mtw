#!/usr/bin/env python
import json
import twitterutl as Utl
from dbConfig   import MongoConf
from pymongo    import Connection


class DataProc(object) :
  def __init__(self, configfile):
    fileHandle          = open(configfile, 'r')
    self.conf           = json.load(fileHandle)
    self.connection     = Connection(self.conf['host'],self.conf['port'])
    self.db = {}
    for dbname in self.conf['dbname']:
      self.db[dbname]   = self.connection[dbname]
    #  for collection in self.conf[dbname]:
    #    self.collections[dbname][collection] = self.db[collection]

    
  def findmatch(self, tweet):
    match_dbname      = []
    match_collection  = []
    #print 'in find match'
    for dbname in self.conf['dbname']:
      #print dbname
      for term in self.conf[dbname]:
        #print "term: %s\n text:%s\n" %(term, tweet)
        if -1 != tweet.lower().find(term.lower()):      
          # print "term: %s\n text:%s\n" %(term, tweet)
          match_dbname.append(dbname)
          match_collection.append(term)

    return (match_dbname, match_collection)

  def process(self, tweet):
    tweet = json.loads(tweet)
    twi   = Utl.processTweetStream(tweet)
    # what's the fuck!!!
    twi   = json.loads(twi)
    (match_dbname, match_collection) = self.findmatch(twi['text'])
    for i in range(0, len(match_dbname)):
      self.db[match_dbname[i]][match_collection[i]].insert(twi)
      # print tweet
    #for match_dbname in matcher:
    #  if None == self.db[self.db][match].find_one({"id":tweet['id']}):
    #    self.db[]


