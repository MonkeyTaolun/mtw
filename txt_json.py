#!/usr/bin/env python


import json
import sys
import logging

def convert(doc, jsonfile):
  try:
    fileHandle_text = open(doc, 'r')
    fileHandle_json = open(jsonfile, 'w')
  except IOError:
    logging.err("loading file error")
    exit()
  sss = fileHandle_text.read()
  sss = sss.replace('}{', '}\n{')
  fileHandle_json.write(sss)
  fileHandle_text.close()
  fileHandle_json.close()

if '__main__' == __name__:
  doc       = sys.argv[1]
  jsonfile  = sys.argv[2]

  convert(doc, jsonfile)
  
