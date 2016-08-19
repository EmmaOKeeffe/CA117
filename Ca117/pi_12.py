import sys

import math

def change(n):
   return '{:.{:d}f}'.format(math.pi, n)

def main():
   print(change(int(sys.argv[1])))

if __name__ == "__main__":
   main()


