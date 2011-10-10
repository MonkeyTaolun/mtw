#!/usr/bin/env python

import urllib
import simplejson
import sys
#import os.path as pt


def googleSearch(query):
  query = urllib.urlencode({'q' : query}) 

  #print query
  jsonsList = []
  for j in range(0, 8):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?start='+str(j*8)+'&rsz=large&v=1.0&%s' \
        % (query)
   
    search_results = urllib.urlopen(url)
    json = simplejson.loads(search_results.read())
    if (json['responseStatus'] == 200) :
      results = json['responseData']['results']
      for result in results :
        jsonsList.append(simplejson.dumps('{"%s" : "%s"}'%(result['titleNoFormatting'] , result['url'])))
        #simplejson.dumps('{"%s" : "%s"}' %(result['titleNoFormatting'] , result['url']))
  return jsonsList

if __name__ == "__main__":
  if len(sys.argv) < 2:
    print 'query missing'
    print googleSearch("food+princing")
  else:
    query = sys.argv[1]
    print googleSearch(query)
