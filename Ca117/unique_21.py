import sys


def count(s):
   l = [] 
   for m in s:
      if m.isdigit() == False and m.isalpha() == False:
         
   for i in s:
      words = i.split()
      for e in words:
         e = e.lower()
         if e not in l:
            l.append(e)

   return (len(l))

def main():
   s = sys.stdin.readlines()
   print (count(s))


if __name__ == "__main__":
   main()
