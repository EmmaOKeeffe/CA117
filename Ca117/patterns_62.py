import sys
import re

def main():
   f = sys.stdin.read()
   p = (re.compile("\d{1,2}/\d{1,2}/\d{2}"))
   print (p.findall(f))
   q = (re.compile("\d{1,2}-\d{1,2}-\d{2}"))
   print (q.findall(f))
   p_q = (re.compile("\d{1,2}[/-]\d{1,2}[/-]\d{2}"))
   print (p_q.findall(f))
   r = (re.compile("01[\s-]\d{7}"))
   print (r.findall(f))
   s = re.compile("(?:\w+\.)*\w+\@\w+\.\w+(?:\.\w+)*")
   print (s.findall(f))
   t = (re.compile("\d{1,2}\s\S{3}\s\d{1,2}"))
   print (t.findall(f))

if __name__ == "__main__":
   main()
