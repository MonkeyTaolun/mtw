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
  def __init__(self, tag, max_id = 200, interval=10):
    self.max_id = max_id
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
      exit() 
    return None

  def crawl(self):
    # there should be some bug
    while(len(self.result) < self.max_id):
      logging.info("Starting search")
      data = self.search()
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
