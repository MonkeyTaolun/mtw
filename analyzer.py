#!/usr/bin/env python

import re
import operator
class Analyzer(object):
  def __init__(self, textfile, tagfile, weight = 10):
    try:
      fileHandle  = open(textfile, 'r')
      text        = fileHandle.read()
      fileHandle.close()
      fileHandle  = open(tagfile, 'r')
      tag         = fileHandle.read()
      fileHandle.close()
    except IOError:
      logging.err('loading error')
      exit()
    

    self.words  = re.split('\W+', text)
    self.tags   = re.split('[^A-Za-z]+', tag)
    self.weight = weight
  def process(self):
    mydict = {}
    self.totalweight = len(self.words) + self.weight * len(self.tags)
    for word in self.words:
      if mydict.has_key(word):
        mydict[word] = mydict[word] + 1
      else:
        mydict[word] = 1
    for tag in self.tags:
      if mydict.has_key(tag):
        mydict[tag] = mydict[tag] + self.weight
      else:
        mydict[tag] = self.weight
     for key in mydict.keys():
        mydict[key] = (float)mydict[key] / self.totalweight

      self.sortedList =sorted(mydict, key=lambda key: mydict[key])

  def analysis(self, num):
    return self.sortedList[:num]


    


