#!/usr/bin/env python
import json
import twitterutl as Utl

class DummyDataProc(object) :
 
  def process(self, tweets):
 
    #for tweet in tweets:
    print 'tweet'
    #stuff = Utl.processTweetJson(tweets)
    
    print tweets['text']
