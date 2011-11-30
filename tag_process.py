#!/usr/bin/env python
import logging
import re
import sys

def convert(before, after):
  try:
    b_file = open(before, 'r')
    a_file = open(after,  'w')
  except IOError:
    logging.err('openfile error')
    exit()

  s = b_file.read()
  s = s.replace('indices', '')
  s = s.replace('text', '')
  a_file.write(s)


if '__main__' == __name__ :
  before    = sys.argv[1] 
  after     = sys.argv[2]

  convert(before, after)

