#!/usr/bin/env python
import httplib
import json
import logging
import socket
import time
import urllib

import twitterutl as utl

SEARCH_HOST="search.twitter.com"
SEARCH_PATH="/search.json"


class SearchCrawler(object):
  def __init__(self, tag, max_id = 2000, interval=25, times = 100):
    self.max_id = max_id
    self.max_time = times
    self.currenttime = 0
    self.tag = tag
    self.interval = interval
    self.result = []
    self.since_id = 0

  def search(self):
    c = httplib.HTTPConnection(SEARCH_HOST)
    params = {'q' : self.tag}
    params['since_id'] = self.since_id
    
    path = "%s?%s" %(SEARCH_PATH, urllib.urlencode(params))
    try:
      c.request('GET', path)
      r = c.getresponse()
      data = r.read()
      c.close()
      try:
        tweet  = json.loads(data)
        self.since_id = tweet['max_id']
      except ValueError, KeyError:
        return None
      for twi in tweet['results']:
        self.result.append(utl.processTweetJson(twi))
    except (httplib.HTTPException, socket.error, socket.timeout), e:
      logging.error("search() error: %s" %(e))
      pass
    time.sleep(self.interval)
    return data

  def crawl(self):
    # there should be some bug
    while(len(self.result) < self.max_id):
      if(self.currenttime > self.max_time): 
        logging.info("runs 100 times")
        break 
      print "currenttime is %d" %(self.currenttime)
      
      logging.info("Starting search")
      data = self.search()
      self.currenttime = self.currenttime  + 1
      
      if data:
        logging.info("%d new result(s)" %(len(data)))
      else:
        logging.info("No new results")
        break;
      #  logging.info("Search complete sleeping for %d seconds" %(self.interval))
      #  time.sleep(float(self.interval))
    
    return self.result
#
#  def submit(self, data):
#    json = json.loads(data)
#    print json
#
if __name__ == '__main__':
  crawler = SearchCrawler('food price',20 ,5)
  result = crawler.crawl()
  for tweet in result:
    twi = json.loads(tweet)
    print twi
    print twi['tid']
    #print tweet['tid']
