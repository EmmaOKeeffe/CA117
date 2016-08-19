import sys

def within(s, t):
    if t in s: 
       print (True)
    else: 
       print(False)

def main():
   s = sys.argv[1]
   t = sys.argv[2]
   within(s, t)


if __name__ == "__main__":
   main()
