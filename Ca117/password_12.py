#isdigit() - at least one digit
#islower - at least one lowercase
#isupper - at least one uppercase
#isalpha, isdigit, isspace

import sys


def password(s):
   i = 0 
   hasdigit = False
   haslower = False
   hasupper = False
   hasspecialchar = False
   while i < len(s): 
      if s[i].isdigit():
         hasdigit = True
      elif s[i].islower():
         haslower = True
      elif s[i].isupper():
         hasupper = True
      else:
         hasspecialchar = True
      i += 1

   return hasdigit + haslower + hasupper + hasspecialchar


def main():
   print (password(sys.argv[1]))


if __name__ == "__main__":
   main()
