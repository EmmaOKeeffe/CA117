import sys 

def middle(s):
    i = len(s) / 2
    i = int(i)
    return s[i]

def main():
   s = sys.argv[1]
   
   if len(s) % 2 != 0 and len(s) > 0:
      print (middle(s))
 
   else:
      print ("No middle character!")
   

if __name__ == "__main__":
   main()

