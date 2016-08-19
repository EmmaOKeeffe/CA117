import sys
import math

def sumFac(n):
   n = int(n)
   l = []
   for i in range(1, n):
      if n % i == 0:
         l.append(i)
   
   isPerfect(sum(l), n)


def isPerfect(s, n):
   if s == n:
      print (True)
   else:
      print (False)

   

def main():
   for line in sys.stdin:
      sumFac(line)

if __name__ == "__main__":
   main()
