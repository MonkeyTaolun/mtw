#!/usr/bin/env python

import twitter 
import json
import logging

import twitterutl     as  Utl
import time
class TwitterCrawler(object) :
  
  def __init__(self, conf, interval = 11):
    #self.dbconf = dbconf
    self.interval = interval
    try:
      fileHandle = open(conf);
    except  IOError:
      logging.error("Loading config file: %s  error" %(conf))
      exit()
    conf = json.load(fileHandle)
    self.api = twitter.Api(
      consumer_key        = conf['consumer_key'], 
      consumer_secret     = conf['consumer_secret'],
      access_token_key    = conf['access_key'],
      access_token_secret = conf['access_secret'],
    )

  def getByUserID(self, userid):
    #followerIDs = self.api.GetFollowerIDs(userid)
    friendstweets = []
    tweets  = []
    print "get user id %d" %(userid)
    time.sleep(self.interval)
    try:
      ftweets = self.api.GetFriendsTimeline(userid)

      for tweet in ftweets:
        friendstweets.append(Utl.processTweetObj(tweet))

      utweets = self.api.GetUserTimeline(userid)
      for tweet in utweets:
        tweets.append(Utl.processTweetObj(tweet))
    except Exception as e:
      logging.error("getByUserID() error: %s" %(e))
      print 'error ! %s' %(e)
      pass
    
    return {'friendstweets' : friendstweets, 'usertweets' : tweets}
   
  def getAPI(self):
    return self.api
  #def 

  #def post(self, twi):

if __name__ == '__main__':
  
  crawler = TwitterCrawler('tweetconf.json')
  tweets  = crawler.getByUserID(361737553)
  print "user tweets"
  for twi in tweets['usertweets']:
    print twi
  print 
  print "user friends tweets"
  for twi in tweets['friendstweets']:
    print twi



