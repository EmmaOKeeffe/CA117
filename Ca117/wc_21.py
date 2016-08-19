import sys


def count(s):
   total = 0 

   for i in s:
      words = i.split()
      total += len(words)

   return (total)

def main():
   s = sys.stdin.readlines()
   print (count(s))

if __name__ == "__main__":
   main()
