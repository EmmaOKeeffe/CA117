import sys

def anagram(f):
   details = f.split()
   first = details[0]
   second = details[1]
   has = True
   i = 0 
   while i < len(first):
      if first[i] not in second:
         has = False 
      else:
         second = second.replace(first[i], "", 1)
      i += 1

   return has


def main():
   f = sys.stdin.readline()
   while f:
      print (anagram(f))
      f = sys.stdin.readline()

if __name__ == "__main__":
   main()

