import sys
import random 

def lotto_numbers(p):
   a = []
   for l in range(10):
      l = []
      for i in range(6):
         l.append(random.randint(1, 47))
      a.append(l)
   
   count = [0]*6
   for n in p:
      if n in a:
         count += 1
   
   print (count)
   print (a)
   print (p)

def main():
   s1 = int(sys.argv[1])
   s2 = int(sys.argv[2])
   s3 = int(sys.argv[3])
   s4 = int(sys.argv[4])
   s5 = int(sys.argv[5])
   s6 = int(sys.argv[6])
   winning = [s1, s2, s3, s4, s5, s6]
   lotto_numbers(winning)

   #print ("Match 3's : {}".format())
   #print ("Match 4's : {}".format())
   #print ("Match 5's : {}".format())
   #print ("Match 6's : {}".format())



if __name__ == "__main__":
   main()
