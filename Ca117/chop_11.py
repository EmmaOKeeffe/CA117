import sys 

def chop(s):
   return s[1:-1]

def main():
   chopped = chop(sys.argv[1])
   if chopped:
      print (chopped)


if __name__ == "__main__":
   main()
