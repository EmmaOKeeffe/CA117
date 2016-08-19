import sys
import string

d = {}

def main():
   s = sys.stdin.read().lower()
   for c in s:
      if c.isalnum() == False and c != "'" and c != " " and c != "\n":
         s = s.replace(c, "")
   
   a = s.split()
   
   for c in a:
      counts = a.count(c)
      d[c] = counts

   for (k, v) in sorted(d.items()):
      print ("{} : {}".format(k, v))
      

if __name__ == "__main__":
   main()
