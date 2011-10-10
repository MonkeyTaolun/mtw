#!/usr/bin/env python

import json

def processTweetJson(twi):
  return json.dumps({'uid': twi['from_user_id'], 'text' : twi['text'], 'geo': twi['geo'], 'time': twi['created_at'], 'tid' : twi['to_user_id'], 'id' : twi['id']})


def processTweetObj(twi):
  #print twi
  return json.dumps({'uid': twi.GetUser().GetId(), 'text' : twi.GetText(), 'geo' : twi.GetGeo(), 'time' : twi.GetCreatedAt() , 'tid' : twi.GetInReplyToUserId(), 'id' : twi.GetId() })
