import sys

def swap(s):
   l = []
   for c in s:
      l.append(c)

   i = 0
   while i < len(l) - 1:
      j = i + 1
      tmp = l[i]
      l[i] = l[j]
      l[j] = tmp
      i += 2

   t = ""
   for f in l:
      t += f
   return t

def main():
   print(swap(sys.argv[1]))



if __name__ == "__main__":
  main()
