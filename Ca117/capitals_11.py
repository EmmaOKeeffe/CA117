import sys 

def upper_case(s):
    if len(s) > 1:
       t = s[0].upper() + s[1:len(s) - 1] + s[len(s) - 1].upper()
       return t

def main():
   capitalized = upper_case(sys.argv[1])
   if capitalized:
      print (capitalized)
   

if __name__ == "__main__":
   main()
