import sys
import math

def Quad(a, b, c):
   r1 = (-b + ((b**2) - 4*a*c)**0.5) / (2*a)
   r2 = (-b - ((b**2) - 4*a*c)**0.5) / (2*a)
   
   if type(r1) == float and type(r2) == float:
      print ("r1 = {}, r2 = {}".format(r1, r2))

   else:
     print (None)


def main():
   for line in sys.stdin:
      details = line.split(" ")
      a = int(details[0])
      b = int(details[1])
      c = int(details[2])
      Quad(a, b, c)

if __name__ == "__main__":
   main()
