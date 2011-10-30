#!/usr/bin/env python

import json
def getHref(twi):
  text        = twi['text']
  herf_s      = text.find('http://')
  if(-1 == herf_s) return None
  herf        = text[herf_s:]
  herf_e      = herf.find(' ')
  if(-1 == herf_e) return herf
  return herf[:herf_e]
  

def getHashTag(twi):
  text        = twi['text']
  tag_s       = text.find('#')
  if(-1 == tag_s) return None
  tag         = text[tag_s:]
  tag_e       = text.find(' ')
  if(-1 == tag_e) return tag
  return tag[:tag_e]

def processTweetJson(twi):
  return json.dumps(
    {
      'uid' : twi['from_user_id'], 
      'text': twi['text'], 
      'geo' : twi['geo'], 
      'time': twi['created_at'], 
      'tid' : twi['to_user_id'], 
      'id'  : twi['id'], 
      'url' :  
    }
  )

def processTweetObj(twi):
  #print twi
  return json.dumps(
    {
      'uid' : twi.GetUser().GetId(), 
      'text': twi.GetText(), 
      'geo' : twi.GetGeo(), 
      'time': twi.GetCreatedAt() , 
      'tid' : twi.GetInReplyToUserId(), 
      'id'  : twi.GetId(), 
      'url' : href 
    }
  )
