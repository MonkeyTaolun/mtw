#!/usr/bin/env python

import sys
import re
import operator

class TF_IDF(object):
  def __init__(self, public_file, item_file):
    try:
      fileHandle          = open(public_file, 'r')
      self.public_lines   = fileHandle.readlines()
      fileHandle.close()
      fileHandle          = open(item_file, 'r')
      self.item_lines      = fileHandle.readlines()
      fileHandle.close()
    except IOError:
      logging.err('loading error')
      exit()
    self.process()

  def addtodict(self, mydict, word):
    word  = word.strip()
    if mydict.has_key(word):
      mydict[word] = mydict[word] + 1
    else:
      mydict[word] = 1

  def createDict(self, lines, mydict):
    for line in lines:
      line  = line.strip()
      line  = line.lower()
#      splited_words = re.split('; |, | |\@|\n|;|,|\. |\#|\?|\!|\$|\%|\^|\&|\*', line)
      splited_words = re.split('[^A-Za-z]+', line)
      for word in splited_words:
        self.addtodict(mydict, word)

  def process(self):
    publicdict  = {}
    itemdict    = {}
    editdict    = {}
    self.createDict(self.public_lines, publicdict)
    self.createDict(self.item_lines, itemdict)

    self.sortedPublic = []
    self.sortedItem   = []
    for word in sorted(publicdict, key=publicdict.get, reverse=True):
      self.sortedPublic.append((word, publicdict[word]))
    for word in sorted(itemdict, key=itemdict.get, reverse=True):
      self.sortedItem.append((word, itemdict[word]))

    for word in itemdict:
      if word in publicdict:
        divider = 1.0 * publicdict[word]
      else: divider = 1.0

      editdict[word] = 10.0 * itemdict[word] / float(divider);

    self.sortedIF_IDF = []
    for word in sorted(editdict, key=editdict.get, reverse=True):
      self.sortedIF_IDF.append((word, editdict[word]))

  def analysispublic(self, num):
    return self.sortedPublic[:num]
  def analysisitem(self, num):
    return self.sortedItem[:num]
  def analysis(self, num):
    return self.sortedIF_IDF[:num]
  def analysis2(self, num):
    return self.sortedIF_IDF[-num:]
if '__main__' == __name__:
  tf_idf  = TF_IDF(sys.argv[1],  sys.argv[2])
  
  print tf_idf.analysis(100)   
  print ''
  print '--------------------------------'
  print tf_idf.analysis2(100)   
  print 'public time line is'
  print tf_idf.analysispublic(200)
  print 'item time line top 100'
  print tf_idf.analysisitem(200)
