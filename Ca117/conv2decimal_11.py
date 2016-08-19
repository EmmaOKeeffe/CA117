import sys

num = sys.argv[1]
base = sys.argv[2]

if base != "10":
   base = int(base)
   power = 0

   i = len(num)-1

   ans = 0

   while i > -1:
      if int(num[i]) > 0:
         ans += (int(num[i]) * (base**power))

      i -= 1
      power += 1

   print (ans)

elif base == "10": 
   print (num) 
