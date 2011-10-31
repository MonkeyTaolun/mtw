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
  def __init__(self, tag, max_id = 2000, interval=25):
    self.max_id = max_id
    self.max_time = 100
    self.currenttime = 0
    self.tag = tag
    self.interval = interval
    self.result = []

  def search(self):
    c = httplib.HTTPConnection(SEARCH_HOST)
    params = {'q' : self.tag}

    params['since_id'] = len(self.result)
    path = "%s?%s" %(SEARCH_PATH, urllib.urlencode(params))
    try:
      c.request('GET', path)
      r = c.getresponse()
      data = r.read()
      c.close()
      try:
        tweet  = json.loads(data)
      except ValueError:
        return None
      for twi in tweet['results']:
        self.result.append(utl.processTweetJson(twi))
   
    except (httplib.HTTPException, socket.error, socket.timeout), e:
      logging.error("search() error: %s" %(e))
      time.sleep(self.interval)
      pass
    return None

  def crawl(self):
    # there should be some bug
    while(len(self.result) < self.max_id):
      logging.info("Starting search")
      data = self.search()
      if(self.currenttime > self.max_time): 
        logging.info("runs 100 times")
        break 
      self.currenttime = self.currenttime  + 1
      if data:
        logging.info("%d new result(s)" %(len(data)))
      else:
        logging.info("No new results")
        logging.info("Search complete sleeping for %d seconds" %(self.interval))
        time.sleep(float(self.interval))
    
    return self.result
#
#  def submit(self, data):
#    json = json.loads(data)
#    print json
#
if __name__ == '__main__':
  crawler = SearchCrawler('food price',20 ,5)
  result = crawler.crawl()
  print "WTF"
  for tweet in result:
    twi = json.loads(tweet)
    print twi
    print twi['tid']
    #print tweet['tid']
