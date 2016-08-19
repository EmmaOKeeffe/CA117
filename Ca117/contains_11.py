import sys

def contain(s, t):
   has = True
   i = 0 
   while i < len(t):
      if t[i] not in s:
         has = False 
      else:
         s = s.replace(t[i], "", 1)
      i += 1

   return has

def main():
   s = sys.argv[1]
   t = sys.argv[2]
   print (contain(s, t))

if __name__ == "__main__":
   main()
