#!/usr/bin/env python

from  twitterStreaming  import  TwitterStream
from  dataprocesser     import  DataProc
if __name__ == '__main__':
  
  username  = 'monkeytaolun'
  passwd    = 'system'

  stream    = TwitterStream(username, passwd, 'streamconf.json')
  

  processer = DataProc('splitconf.json')

  stream.tracking(processer)
