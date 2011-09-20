#!/usr/bin/env python

import urllib
import simplejson
import sys
#import os.path as pt

def googleSearch(query):
 query = urllib.urlencode({'q' : query}) 

 print query

 for j in range(0, 8):
   url = 'http://ajax.googleapis.com/ajax/services/search/web?start='+str(j*8)+'&rsz=large&v=1.0&%s' \
        % (query)
   
   search_results = urllib.urlopen(url)
   json = simplejson.loads(search_results.read())
   if (json['responseStatus'] == 200) :

   #print json
     results = json['responseData']['results']
     for result in results :
     #print "this is result in whole"
       print result['titleNoFormatting']
       print result['url']
     #for partresult in result :
     #  print partresult
     #print "\n------------------------\n"
   #titles = json['responseData']['results']['titleNoFormatting']
   #urls = json['responseData']['results']['url ']
   #print "titles is %s\n url is %s\n" %(titles, urls) 
   #print "\n\n\n"



if __name__ == "__main__":
  if len(sys.argv) < 2:
    print 'query missing'
    googleSearch("food+princing")
  else:
    query = sys.argv[1]
    googleSearch(query)
