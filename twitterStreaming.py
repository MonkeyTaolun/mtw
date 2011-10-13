#!/usr/bin/env python
import json
import urllib2
import urllib
import getpass
import base64
import logging

from dummyDataProc import DummyDataProc

url='https://stream.twitter.com/1/statuses/filter.json'

class TwitterStream(object) :

  def __init__(self,username, password, data):
    try:
      fileHandle = open(data)
    except IOError:
      logging.error("Loading config file: %s error" %(conf))
      exit()
    self.data     = json.load(fileHandle)
    self.headers  = {}
  
    self.headers['User-Agent'] = 'Mapping the World'
    self.headers['Authorization'] = 'Basic ' + base64.b64encode('%s:%s' % (username, password))
    self.req = urllib2.Request(url, headers=self.headers)
    self.req.add_data(urllib.urlencode(self.data))
  

  def tracking(self, data_pro):
    try:
      f = urllib2.urlopen(self.req)
      while True:
        line = f.readline()
        if line:
          tweets = json.loads(line)
          try:
            data_pro.process(tweets)
          except:
            print "FIX this!!!!", line
            logging.error('error in process data')
        else:
          time.sleep(0.1)
    except urllib2.HTTPError, e:
      logging.error('urllib2 error')
      print 'urllib2.HTTPError'
      raise e
    except KeyboardInterrupt:
      f.close()

if __name__ == '__main__' :
  
  username  = raw_input('username:  ')
  password  = getpass.getpass('password: ')
  stream    = TwitterStream(username, password, 'streamconf.json')

  dummy     = DummyDataProc()
  stream.tracking(dummy)


