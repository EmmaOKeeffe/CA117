import sys
import string
from operator import itemgetter

d = {}

def main():
   s = sys.stdin.read().lower()
   a = []
   for c in s:
      if c in "aeiou":
         a.append(c)
         count = a.count(c)
         d[c] = count
   
   for (k, v) in sorted(d.items(), key=itemgetter(1), reverse = True):
      print ("{} : {:>3d}".format(k, v))
      

if __name__ == "__main__":
   main()
