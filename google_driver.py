from googleSearch import googleSearch
from time import sleep
import cPickle

if __name__ == "__main__":
  term_equal = ("food", "provisions", "nutrition", "nourishment","something+to+eat", "eat", "provisions", "viands", "pabulum", "vivers")

  term_condition = ("price", "availability", "condition", "emergency", "shortage", "waste", "supply", "demand", "quality", "crisis", "riots", "aid")

  for equal in term_equal:
    for condition in term_condition:
#      print "%s+%s" %(equal, condition)
      query = "%s+%s"  %(equal, condition)
      #print query
      results = googleSearch(query)
      cPickle.dump(results,open(query+'.p','wb'))
      sleep(1)
