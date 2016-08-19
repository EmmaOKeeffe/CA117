import sys

def sorter(t):
   return t[1]

def main():
   nums = []
   d = {}
   total = 0 
   count = 0 
   for line in sys.stdin:
      n = int(line.strip())

      if n in d:
         d[n] += 1
      else:
         d[n] = 1

      nums.append(n)
      total += n
      count += 1

   mean = total/count

   snums = sorted(nums)
   N = len(snums)

   if N % 2 == 1:
      median = snums[N/2]
   else:
      median = (snums[N//2-1] + snums[N//2])/2

   mode_tuple = max(d.items(), key=sorter)
   mode = mode_tuple[0]

   print ("Mean: {:.1f}".format(mean))
   print ("Median: {:.1f}".format(median))
   print ("Mode: {:.1f}".format(mode))


if __name__ == "__main__":
   main()
