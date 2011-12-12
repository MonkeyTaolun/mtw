#!/usr/bin/env python
import sys
import re
import operator
class Analyzer(object):
  def __init__(self, textfile, tagfile, gram = 2):
    try:
      fileHandle  = open(textfile, 'r')
      self.lines  = fileHandle.readlines()
      fileHandle.close()
      fileHandle  = open(tagfile, 'r')
      tag         = fileHandle.read()
      fileHandle.close()
    except IOError:
      logging.err('loading error')
      exit()
    
    self.gram   = gram
    self.tags   = re.split('[^A-Za-z]+', tag)
    
    self.process()

  def addtodict(self, mydict, word):
    word = word.strip()
    if mydict.has_key(word):
      mydict[word] = mydict[word] + 1
    else:
      mydict[word] = 1

  def process(self):
    mydict = {}
    for line in self.lines:
      #print line
      line  = line.strip() 
      line  = line.lower() 
      words = re.split('\W+', line)
      if self.gram > len(words):
        continue
      sentence = ''
      for i in range(self.gram - 1):
        word = words[i]
        sentence = sentence + words[i] + ' '
      for i in range(self.gram - 1, len(words)):
        if len(words[i]) < 3:
            continue
        sentence = sentence + words[i] + ' '  
        self.addtodict(mydict, sentence)
        sentence = sentence[ sentence.find(' ') + 1 :]
    mytag = {}
    for tag in self.tags:
      tag = tag.strip()
      tag = tag.lower()
      if (tag == 'text' or tag == 'indices') :
        continue
      self.addtodict(mytag, tag)
    
    self.sortedGram = []
    self.sortedTag  = []
    for w in sorted(mydict, key=mydict.get, reverse=True):
      self.sortedGram.append((w, mydict[w]))
    for t in sorted(mytag, key=mytag.get, reverse=True):
      self.sortedTag.append((t, mytag[t]))

  def analysisGram(self, num):
    print "This is %d gram result\n" %(self.gram)
    return self.sortedGram[:num]

  def analysisTag(self, num):
    print "This is Top Tag\n"
    return self.sortedTag[:num]
if '__main__' == __name__:
  
  analyzer = Analyzer(sys.argv[1],  sys.argv[2], 2)
  print analyzer.analysisGram(200)
  print analyzer.analysisTag(10)

