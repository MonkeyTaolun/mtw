#!/usr/bin/env python

from pymongo import Connection

import json
import logging

class MongoConf(object):
  def __init__(self, keyword, conf):
    try:
      fileHandle = open(conf)
    except IOError:
      logging.err("Loading config file: %s error" %(conf))
      exit()
    self.conf = json.load(fileHandle)
    self.connection = Connection(self.conf['host'], self.conf['port'])
    self.db = self.connection[self.conf['dbname']]
    self.posts = self.db[keyword]
  
  def insert(self, tweet):
    if None == self.posts.find_one({"id": tweet['id']}):
      self.posts.insert(tweet)
    #  print "inserted it"
    #else: 
    #  print "duplicate"



if __name__ == "__main__":
  mongo = MongoConf('mongoconfig.json')

