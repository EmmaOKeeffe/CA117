import sys

def palindrome(f):
   i = 0 
   while i < len(f)/2:
      if f[i] != f[-( i+ 1)]:
         return False
      i += 1  

   return True

def main():
   f = sys.argv[1]
   for c in  f:
      if c.isalpha() == False:
         f = f.replace(c, "")

   print (palindrome(f.lower()))


if __name__ == "__main__":
   main()
